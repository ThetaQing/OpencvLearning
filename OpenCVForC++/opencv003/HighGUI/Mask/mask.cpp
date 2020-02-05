#include <opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>  
#include<opencv2/imgproc/imgproc.hpp>  
#include <iostream>  

using namespace cv;
using namespace std;

Mat getFFTresultImg(Mat& completeI, CvSize srcSize)
{
	Mat planes[2];
	split(completeI, planes);//�ѱ任��Ľ���ָ�����������ҳ�У������������ 
	Mat magI;
	magnitude(planes[0], planes[1], magI);//����Ҷ�任��Ƶ�ʵķ�ֵ����ֵ���ڵ�һҳ�С�  


	//����Ҷ�任�ķ���ֵ��Χ�󵽲��ʺ�����Ļ����ʾ����ֵ����Ļ����ʾΪ�׵㣬  
	//����ֵΪ�ڵ㣬�ߵ�ֵ�ı仯�޷���Ч�ֱ档Ϊ������Ļ��͹�Գ��ߵͱ仯�������ԣ����ǿ����ö����߶����滻���Գ߶�:  
	magI += 1;
	log(magI, magI);//ȡ����  
	magI = magI(Rect(0, 0, srcSize.width, srcSize.height));//ǰ�߶�ԭʼͼ���������չ������Ѷ�ԭʼͼ����Ҷ�任ȡ�����޳���չ���֡�  


	//��һ����Ŀ����Ȼ��Ϊ����ʾ�� �������������طֲ���ķ���ͼ��  
	//���Ƿ���ֵ��Ȼ��������ʾ��Χ[0,1] ������ʹ�� normalize() ���������ȹ�һ��������ʾ��Χ��  
	normalize(magI, magI, 0, 1, CV_MINMAX);//����Ҷͼ����й�һ����  


	//���·������ޣ�ʹ��0,0���ƶ���ͼ�����ģ�  
	//�ڡ�����ͼ�����У�����Ҷ�任֮ǰҪ��Դͼ����ԣ�-1��^(x+y)�������Ļ���  
	//�����ǶԸ���Ҷ�任����������Ļ�  
	int cx = magI.cols / 2;
	int cy = magI.rows / 2;

	Mat tmp;
	Mat q0(magI, Rect(0, 0, cx, cy));
	Mat q1(magI, Rect(cx, 0, cx, cy));
	Mat q2(magI, Rect(0, cy, cx, cy));
	Mat q3(magI, Rect(cx, cy, cx, cy));


	q0.copyTo(tmp);
	q3.copyTo(q0);
	tmp.copyTo(q3);

	q1.copyTo(tmp);
	q2.copyTo(q1);
	tmp.copyTo(q2);
	return magI;
}

Mat FFT(Mat& src_gray)
{
	//Mat src_gray;
	//cvtColor(src, src_gray, CV_RGB2GRAY);//�Ҷ�ͼ��������Ҷ�任  

	int m = getOptimalDFTSize(src_gray.rows);//2,3,5�ı����и���Ч�ʵĸ���Ҷת��  
	int n = getOptimalDFTSize(src_gray.cols);

	Mat dst;
	///�ѻҶ�ͼ��������Ͻǣ����ұߺ��±���չͼ����չ�������Ϊ0��  
	// 0, m - src_gray.rows, 0, n - src_gray.cols �ϱ����0�У��������m - src_gray.rows��
	copyMakeBorder(src_gray, dst, 0, m - src_gray.rows, 0, n - src_gray.cols, BORDER_CONSTANT, Scalar::all(0));
	//cout << dst.size() << endl;

	//�½�һ����ҳ��array�����е�һҳ����չ���ͼ���ʼ�����ڶ�ҳ��ʼ��Ϊ0  
	Mat planes[] = { Mat_<float>(dst), Mat::zeros(dst.size(), CV_32F) };
	Mat  completeI;
	merge(planes, 2, completeI);//����ҳ�ϳ�һ��2ͨ����mat  

	//���ϱߺϳɵ�mat���и���Ҷ�任��֧��ԭ�ز���������Ҷ�任���Ϊ������ͨ��1�����ʵ����ͨ��2������鲿��  
	dft(completeI, completeI);


	return completeI.clone();
}
//�����˹�˲�ϵ������
Mat clcGLPFMat(Mat& mat, int D0)
{
	int width = mat.rows;
	int height = mat.cols;
	int M = width;
	int N = height;
	Mat mat_GLPF(mat.size(), CV_32FC1);

	Mat U, V;
	U.create(M, N, CV_32FC1);
	V.create(M, N, CV_32FC1);

	for (int u = 0; u < M; ++u)
	{
		for (int v = 0; v < N; ++v)
		{
			float tm1, tm2;
			tm1 = (float)((u > cvRound(M / 2)) ? u - M : u);
			tm2 = (float)((v > cvRound(N / 2)) ? v - N : v);

			U.at<float>(u, v) = tm1;
			V.at<float>(u, v) = tm2;
		}
	}


	for (int u = 0; u < M; ++u)
	{
		for (int v = 0; v < N; ++v)
		{
			float t1, t2;
			t1 = U.at<float>(u, v);
			t2 = V.at<float>(u, v);
			float Elem_D = t1 * t1 + t2 * t2;
			mat_GLPF.at<float>(u, v) = (float)(exp(-(Elem_D) / (2 * D0 * D0)) / 2 / 3.1415 / (2 * D0 * D0));
		}
	}
	Mat_<float>::iterator begainIt = mat_GLPF.begin<float>();
	Mat_<float>::iterator endIt = mat_GLPF.end<float>();
	float sumValue = 0;
	for (; begainIt != endIt; begainIt++)
	{
		sumValue += *begainIt;
	}
	mat_GLPF = mat_GLPF / sumValue;
	return mat_GLPF.clone();
}

Mat mask(Mat& plane)
{
	Mat FFTresult = FFT(plane);//����Ҷ�任����ʵ�����鲿���ֱ��������planes��
	Mat planes[2];
	split(FFTresult, planes);
	imshow("FFTresult", getFFTresultImg(FFTresult, FFTresult.size()));

	Mat GLPFMatIM = clcGLPFMat(planes[0], 10);//��˹�˲�ϵ��
	Mat GLPFMatRE = clcGLPFMat(planes[1], 10);
	planes[0] = GLPFMatIM.mul(planes[0]);
	planes[1] = GLPFMatRE.mul(planes[1]);
	Mat GLPFresult;
	merge(planes, 2, GLPFresult);       //ʵ���鲿�ֱ��˹�˲���Ȼ��ϳɵ��˲����
	imshow("FFTresultAfterFlit", getFFTresultImg(GLPFresult, GLPFresult.size()));

	Mat maskResult;
	dft(GLPFresult, maskResult, DFT_INVERSE + DFT_SCALE);//�˲����������Ҷ���任

	split(maskResult, planes);//�ѷ��任��Ľ���ָ��ҳ�У������������ 
	Mat mask;
	magnitude(planes[0], planes[1], mask);//����Ҷ�任��Ƶ�ʵķ�ֵ  
	return mask.clone();
}


