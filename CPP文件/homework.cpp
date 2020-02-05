#include <opencv2/opencv.hpp>
#include <iostream> 
# include "highgui.hpp"
using namespace cv;
using namespace std;
/*
int test_main()
{
	//读取图片文件
	Mat src = imread("D:/Pic/simple/amazed.png");
	if (src.empty())
	{
		printf("文件不存在。。。");
		return -1;
	}	//创建一个窗口
	namedWindow("test opencv setup", CV_WINDOW_AUTOSIZE);	//在窗口中显示图片
	imshow("test opencv setup", src);	//在一个给定的时间内(单位ms)等待用户按键触发;如果用户没有按下 键,则接续等待(循环)
										//waitKey(0)无限循环等待
	waitKey(0);
	return 0;
}
*/
/*函数名称：rotateImage1(Mat img, int degree)
*函数参数：img为Mat图像，degree为int类型的角度值
*函数功能：实现对输入图像img旋转degree角度
*函数返回值：旋转后的图像
*/
Mat rotateImage1(Mat img, int degree)
{
	degree = -degree;
	double angle = degree * CV_PI / 180.; // 弧度  
	double a = sin(angle), b = cos(angle);
	int width = img.cols;
	int height = img.rows;
	int width_rotate = int(height * fabs(a) + width * fabs(b));
	int height_rotate = int(width * fabs(a) + height * fabs(b));
	//旋转数组map
	// [ m0  m1  m2 ] ===>  [ A11  A12   b1 ]
	// [ m3  m4  m5 ] ===>  [ A21  A22   b2 ]
	float map[6];
	Mat map_matrix = Mat(2, 3, CV_32F, map);
	// 旋转中心
	CvPoint2D32f center = cvPoint2D32f(width / 2, height / 2);
	CvMat map_matrix2 = map_matrix;
	cv2DRotationMatrix(center, degree, 1.0, &map_matrix2);
	map[2] += (width_rotate - width) / 2;
	map[5] += (height_rotate - height) / 2;
	Mat img_rotate;
	//对图像做仿射变换
	//CV_WARP_FILL_OUTLIERS - 填充所有输出图像的象素。
	//如果部分象素落在输入图像的边界外，那么它们的值设定为 fillval.
	//CV_WARP_INVERSE_MAP - 指定 map_matrix 是输出图像到输入图像的反变换，
	warpAffine(img, img_rotate, map_matrix, Size(width_rotate, height_rotate), 1, 0, 0);
	return img_rotate;
}
/*函数名称：createImageFromMatrix(int matrix[])
*函数参数：int matrix[]，int类型的矩阵
*函数功能：创建Mat图像
*函数返回值：Mat类型的图像
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
	namedWindow("原图像", 1);
	imshow("原图像",Pic);
	cout << "请输入旋转的度数：";
	cin >> degree;
	Mat dst = rotateImage1(Pic, degree);
	namedWindow("旋转后的图像", 1);
	imshow("旋转后的图像", dst);

	waitKey(0);
	return 0;




}*/
/*函数名称：
*函数功能：实现图像以 x轴和y轴的错切

int shear_main() {
	float pi = 3.141592653;
	float a = pi / 4;//错切角度	
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
	cvNamedWindow("y_shear", 1);	//显示图像
	cvShowImage("inputimage", inputimage);
	cvShowImage("x_shear", x_shear);
	cvShowImage("y_shear", y_shear);
	cvWaitKey(0);	//保存图像	
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
	//读取图片文件
	Mat src = imread("D:/Pic/simple/amazed.png");
	if (src.empty())
	{
		printf("文件不存在。。。");
		return -1;
	}	//创建一个窗口
	namedWindow("test opencv setup", CV_WINDOW_AUTOSIZE);	//在窗口中显示图片
	imshow("test opencv setup", src);	//在一个给定的时间内(单位ms)等待用户按键触发;如果用户没有按下 键,则接续等待(循环)
										//waitKey(0)无限循环等待
	waitKey(0);
	return 0;
}
*/
/*函数名称：rotateImage1(Mat img, int degree)
*函数参数：img为Mat图像，degree为int类型的角度值
*函数功能：实现对输入图像img旋转degree角度
*函数返回值：旋转后的图像
*/
Mat rotateImage1(Mat img, int degree)
{
	degree = -degree;
	double angle = degree * CV_PI / 180.; // 弧度  
	double a = sin(angle), b = cos(angle);
	int width = img.cols;
	int height = img.rows;
	int width_rotate = int(height * fabs(a) + width * fabs(b));
	int height_rotate = int(width * fabs(a) + height * fabs(b));
	//旋转数组map
	// [ m0  m1  m2 ] ===>  [ A11  A12   b1 ]
	// [ m3  m4  m5 ] ===>  [ A21  A22   b2 ]
	float map[6];
	Mat map_matrix = Mat(2, 3, CV_32F, map);
	// 旋转中心
	CvPoint2D32f center = cvPoint2D32f(width / 2, height / 2);
	CvMat map_matrix2 = map_matrix;
	cv2DRotationMatrix(center, degree, 1.0, &map_matrix2);
	map[2] += (width_rotate - width) / 2;
	map[5] += (height_rotate - height) / 2;
	Mat img_rotate;
	//对图像做仿射变换
	//CV_WARP_FILL_OUTLIERS - 填充所有输出图像的象素。
	//如果部分象素落在输入图像的边界外，那么它们的值设定为 fillval.
	//CV_WARP_INVERSE_MAP - 指定 map_matrix 是输出图像到输入图像的反变换，
	warpAffine(img, img_rotate, map_matrix, Size(width_rotate, height_rotate), 1, 0, 0);
	return img_rotate;
}
/*函数名称：createImageFromMatrix(int matrix[])
*函数参数：int matrix[]，int类型的矩阵
*函数功能：创建Mat图像
*函数返回值：Mat类型的图像
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
	namedWindow("原图像", 1);
	imshow("原图像",Pic);
	cout << "请输入旋转的度数：";
	cin >> degree;
	Mat dst = rotateImage1(Pic, degree);
	namedWindow("旋转后的图像", 1);
	imshow("旋转后的图像", dst);

	waitKey(0);
	return 0;




}*/
/*函数名称：
*函数功能：实现图像以 x轴和y轴的错切
*/
int main() {
	float pi = 3.141592653;
	float a = pi / 4;//错切角度	
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
	cvNamedWindow("y_shear", 1);	//显示图像
	cvShowImage("inputimage", inputimage);
	cvShowImage("x_shear", x_shear);
	cvShowImage("y_shear", y_shear);
	cvWaitKey(0);	//保存图像	
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
