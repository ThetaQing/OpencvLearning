// #include "stdafx.h"

#include <iostream>
#include <opencv2\core\core.hpp>
#include <opencv2\highgui\highgui.hpp>
#include <opencv2\imgproc\imgproc.hpp>

using namespace std;
using namespace cv;
/*线性变换*/
int main()
{
	Mat srcImg = imread("D:/Pic/simple/amazed.png", 0);
	if (!srcImg.data)
	{
		cout << "读入图片失败" << endl;
		return -1;
	}
	double k, b;
	cout << "请输入k和b值：";
	cin >> k >> b;
	int RowsNum = srcImg.rows;
	int ColsNum = srcImg.cols;
	Mat dstImg(srcImg.size(), srcImg.type());
	//进行遍历图像像素,对每个像素进行相应的线性变换
	for (int i = 0; i < srcImg.rows; i++)
	{
		uchar *srcData = srcImg.ptr<uchar>(i);
		for (int j = 0; j < srcImg.cols; j++)
		{
			dstImg.at<uchar>(i, j) = srcData[j] * k + b;
		}
	}
	imshow("原图", srcImg);
	imshow("线性变换后的图像", dstImg);
	waitKey();
	return 0;
}