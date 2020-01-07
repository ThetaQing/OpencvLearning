#include <opencv2/opencv.hpp>
#include <iostream> 
# include "highgui.hpp"
using namespace cv;
using namespace std;
/*
int test_main()
{
	//��ȡͼƬ�ļ�
	Mat src = imread("D:/Pic/simple/amazed.png");
	if (src.empty())
	{
		printf("�ļ������ڡ�����");
		return -1;
	}	//����һ������
	namedWindow("test opencv setup", CV_WINDOW_AUTOSIZE);	//�ڴ�������ʾͼƬ
	imshow("test opencv setup", src);	//��һ��������ʱ����(��λms)�ȴ��û���������;����û�û�а��� ��,������ȴ�(ѭ��)
										//waitKey(0)����ѭ���ȴ�
	waitKey(0);
	return 0;
}
*/
/*�������ƣ�rotateImage1(Mat img, int degree)
*����������imgΪMatͼ��degreeΪint���͵ĽǶ�ֵ
*�������ܣ�ʵ�ֶ�����ͼ��img��תdegree�Ƕ�
*��������ֵ����ת���ͼ��
*/
Mat rotateImage1(Mat img, int degree)
{
	degree = -degree;
	double angle = degree * CV_PI / 180.; // ����  
	double a = sin(angle), b = cos(angle);
	int width = img.cols;
	int height = img.rows;
	int width_rotate = int(height * fabs(a) + width * fabs(b));
	int height_rotate = int(width * fabs(a) + height * fabs(b));
	//��ת����map
	// [ m0  m1  m2 ] ===>  [ A11  A12   b1 ]
	// [ m3  m4  m5 ] ===>  [ A21  A22   b2 ]
	float map[6];
	Mat map_matrix = Mat(2, 3, CV_32F, map);
	// ��ת����
	CvPoint2D32f center = cvPoint2D32f(width / 2, height / 2);
	CvMat map_matrix2 = map_matrix;
	cv2DRotationMatrix(center, degree, 1.0, &map_matrix2);
	map[2] += (width_rotate - width) / 2;
	map[5] += (height_rotate - height) / 2;
	Mat img_rotate;
	//��ͼ��������任
	//CV_WARP_FILL_OUTLIERS - ����������ͼ������ء�
	//�������������������ͼ��ı߽��⣬��ô���ǵ�ֵ�趨Ϊ fillval.
	//CV_WARP_INVERSE_MAP - ָ�� map_matrix �����ͼ������ͼ��ķ��任��
	warpAffine(img, img_rotate, map_matrix, Size(width_rotate, height_rotate), 1, 0, 0);
	return img_rotate;
}
/*�������ƣ�createImageFromMatrix(int matrix[])
*����������int matrix[]��int���͵ľ���
*�������ܣ�����Matͼ��
*��������ֵ��Mat���͵�ͼ��
*/
Mat createImageFromMatrix(int matrix[])
{
	Mat dst = Mat(4, 4, CV_64FC1, matrix);
	return dst;
}
/*
int rotate_main()
{
	int degree;

	Mat sim = imread("D:/Pic/simple/amazed.png");
	int scr[] = {59,60,58,57,
			61,59,59,57,
			62,59,60,58,
			59,61,60,56 };
	Mat Pic = Mat(4, 4, CV_64FC1, scr);
	int width = Pic.cols;
	int height = Pic.rows;
	namedWindow("ԭͼ��", 1);
	imshow("ԭͼ��",Pic);
	cout << "��������ת�Ķ�����";
	cin >> degree;
	Mat dst = rotateImage1(Pic, degree);
	namedWindow("��ת���ͼ��", 1);
	imshow("��ת���ͼ��", dst);

	waitKey(0);
	return 0;




}*/
/*�������ƣ�
*�������ܣ�ʵ��ͼ���� x���y��Ĵ���

int shear_main() {
	float pi = 3.141592653;
	float a = pi / 4;//���нǶ�	
	const char *filename = "D:/Pic/simple/amazed.png";
	IplImage *inputimage = cvLoadImage(filename, -1);
	IplImage *x_shear = cvCreateImage(cvSize((inputimage->width + inputimage->height / tan(a)), inputimage->height), IPL_DEPTH_8U, inputimage->nChannels);
	IplImage *y_shear = cvCreateImage(cvSize(inputimage->width, (inputimage->height + inputimage->width / tan(a))), IPL_DEPTH_8U, inputimage->nChannels);
	for (int i = 0; i < x_shear->height; i++)
	{
		for (int j = 0; j < x_shear->width; j++)
		{
			for (int k = 0; k < x_shear->nChannels; k++)
				if (j < x_shear->height / tan(a) - i / tan(a) || j > x_shear->height / tan(a) - i / tan(a) + inputimage->width)
					x_shear->imageData[i*x_shear->widthStep + j * x_shear->nChannels + k] = 0;
				else
					x_shear->imageData[i*x_shear->widthStep + j * x_shear->nChannels + k] = inputimage->imageData[i*inputimage->widthStep + (j - int(x_shear->height / tan(a) - i / tan(a)))*inputimage->nChannels + k];
		}
	}
	for (int i = 0; i < y_shear->height; i++)
	{
		for (int j = 0; j < y_shear->width; j++)
		{
			for (int k = 0; k < y_shear->nChannels; k++)
				if (i < y_shear->width / tan(a) - j / tan(a) || i > y_shear->width / tan(a) - j / tan(a) + inputimage->height)
					y_shear->imageData[i*y_shear->widthStep + j * y_shear->nChannels + k] = 0;
				else
					y_shear->imageData[i*y_shear->widthStep + j * y_shear->nChannels + k] = inputimage->imageData[(i - int(y_shear->width / tan(a) - j / tan(a)))*inputimage->widthStep + j * inputimage->nChannels + k];
		}
	}
	cvNamedWindow("inputimage", 1);
	cvNamedWindow("x_shear", 1);
	cvNamedWindow("y_shear", 1);	//��ʾͼ��
	cvShowImage("inputimage", inputimage);
	cvShowImage("x_shear", x_shear);
	cvShowImage("y_shear", y_shear);
	cvWaitKey(0);	//����ͼ��	
	cv::Mat amplification1 = cv::cvarrToMat(x_shear);
	cv::Mat amplification2 = cv::cvarrToMat(y_shear);
	cv::imwrite("x_island.bmp", amplification1);
	cv::imwrite("y_island.bmp", amplification2);
	cvDestroyWindow("inputimage");
	cvDestroyWindow("x_shear");
	cvDestroyWindow("y_shear");
	cvReleaseImage(&inputimage);
	cvReleaseImage(&x_shear);
	cvReleaseImage(&y_shear);
}
#include <opencv2/opencv.hpp>
#include <iostream>
# include "highgui.hpp"
using namespace cv;
using namespace std;
/*
int main()
{
	//��ȡͼƬ�ļ�
	Mat src = imread("D:/Pic/simple/amazed.png");
	if (src.empty())
	{
		printf("�ļ������ڡ�����");
		return -1;
	}	//����һ������
	namedWindow("test opencv setup", CV_WINDOW_AUTOSIZE);	//�ڴ�������ʾͼƬ
	imshow("test opencv setup", src);	//��һ��������ʱ����(��λms)�ȴ��û���������;����û�û�а��� ��,������ȴ�(ѭ��)
										//waitKey(0)����ѭ���ȴ�
	waitKey(0);
	return 0;
}
*/
/*�������ƣ�rotateImage1(Mat img, int degree)
*����������imgΪMatͼ��degreeΪint���͵ĽǶ�ֵ
*�������ܣ�ʵ�ֶ�����ͼ��img��תdegree�Ƕ�
*��������ֵ����ת���ͼ��
*/
Mat rotateImage1(Mat img, int degree)
{
	degree = -degree;
	double angle = degree * CV_PI / 180.; // ����  
	double a = sin(angle), b = cos(angle);
	int width = img.cols;
	int height = img.rows;
	int width_rotate = int(height * fabs(a) + width * fabs(b));
	int height_rotate = int(width * fabs(a) + height * fabs(b));
	//��ת����map
	// [ m0  m1  m2 ] ===>  [ A11  A12   b1 ]
	// [ m3  m4  m5 ] ===>  [ A21  A22   b2 ]
	float map[6];
	Mat map_matrix = Mat(2, 3, CV_32F, map);
	// ��ת����
	CvPoint2D32f center = cvPoint2D32f(width / 2, height / 2);
	CvMat map_matrix2 = map_matrix;
	cv2DRotationMatrix(center, degree, 1.0, &map_matrix2);
	map[2] += (width_rotate - width) / 2;
	map[5] += (height_rotate - height) / 2;
	Mat img_rotate;
	//��ͼ��������任
	//CV_WARP_FILL_OUTLIERS - ����������ͼ������ء�
	//�������������������ͼ��ı߽��⣬��ô���ǵ�ֵ�趨Ϊ fillval.
	//CV_WARP_INVERSE_MAP - ָ�� map_matrix �����ͼ������ͼ��ķ��任��
	warpAffine(img, img_rotate, map_matrix, Size(width_rotate, height_rotate), 1, 0, 0);
	return img_rotate;
}
/*�������ƣ�createImageFromMatrix(int matrix[])
*����������int matrix[]��int���͵ľ���
*�������ܣ�����Matͼ��
*��������ֵ��Mat���͵�ͼ��
*/
Mat createImageFromMatrix(int matrix[])
{
	Mat dst = Mat(4, 4, CV_64FC1, matrix);
	return dst;
}
/*
int main()
{
	int degree;

	Mat sim = imread("D:/Pic/simple/amazed.png");
	int scr[] = {59,60,58,57,
			61,59,59,57,
			62,59,60,58,
			59,61,60,56 };
	Mat Pic = Mat(4, 4, CV_64FC1, scr);
	int width = Pic.cols;
	int height = Pic.rows;
	namedWindow("ԭͼ��", 1);
	imshow("ԭͼ��",Pic);
	cout << "��������ת�Ķ�����";
	cin >> degree;
	Mat dst = rotateImage1(Pic, degree);
	namedWindow("��ת���ͼ��", 1);
	imshow("��ת���ͼ��", dst);

	waitKey(0);
	return 0;




}*/
/*�������ƣ�
*�������ܣ�ʵ��ͼ���� x���y��Ĵ���
*/
int main() {
	float pi = 3.141592653;
	float a = pi / 4;//���нǶ�	
	const char *filename = "D:/Pic/simple/amazed.png";
	IplImage *inputimage = cvLoadImage(filename, -1);
	IplImage *x_shear = cvCreateImage(cvSize((inputimage->width + inputimage->height / tan(a)), inputimage->height), IPL_DEPTH_8U, inputimage->nChannels);
	IplImage *y_shear = cvCreateImage(cvSize(inputimage->width, (inputimage->height + inputimage->width / tan(a))), IPL_DEPTH_8U, inputimage->nChannels);
	for (int i = 0; i < x_shear->height; i++)
	{
		for (int j = 0; j < x_shear->width; j++)
		{
			for (int k = 0; k < x_shear->nChannels; k++)
				if (j < x_shear->height / tan(a) - i / tan(a) || j > x_shear->height / tan(a) - i / tan(a) + inputimage->width)
					x_shear->imageData[i*x_shear->widthStep + j * x_shear->nChannels + k] = 0;
				else
					x_shear->imageData[i*x_shear->widthStep + j * x_shear->nChannels + k] = inputimage->imageData[i*inputimage->widthStep + (j - int(x_shear->height / tan(a) - i / tan(a)))*inputimage->nChannels + k];
		}
	}
	for (int i = 0; i < y_shear->height; i++)
	{
		for (int j = 0; j < y_shear->width; j++)
		{
			for (int k = 0; k < y_shear->nChannels; k++)
				if (i < y_shear->width / tan(a) - j / tan(a) || i > y_shear->width / tan(a) - j / tan(a) + inputimage->height)
					y_shear->imageData[i*y_shear->widthStep + j * y_shear->nChannels + k] = 0;
				else
					y_shear->imageData[i*y_shear->widthStep + j * y_shear->nChannels + k] = inputimage->imageData[(i - int(y_shear->width / tan(a) - j / tan(a)))*inputimage->widthStep + j * inputimage->nChannels + k];
		}
	}
	cvNamedWindow("inputimage", 1);
	cvNamedWindow("x_shear", 1);
	cvNamedWindow("y_shear", 1);	//��ʾͼ��
	cvShowImage("inputimage", inputimage);
	cvShowImage("x_shear", x_shear);
	cvShowImage("y_shear", y_shear);
	cvWaitKey(0);	//����ͼ��	
	cv::Mat amplification1 = cv::cvarrToMat(x_shear);
	cv::Mat amplification2 = cv::cvarrToMat(y_shear);
	cv::imwrite("x_island.bmp", amplification1);
	cv::imwrite("y_island.bmp", amplification2);
	cvDestroyWindow("inputimage");
	cvDestroyWindow("x_shear");
	cvDestroyWindow("y_shear");
	cvReleaseImage(&inputimage);
	cvReleaseImage(&x_shear);
	cvReleaseImage(&y_shear);
}
