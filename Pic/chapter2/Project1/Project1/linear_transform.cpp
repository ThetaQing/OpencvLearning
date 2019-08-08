// #include "stdafx.h"

#include <iostream>
#include <opencv2\core\core.hpp>
#include <opencv2\highgui\highgui.hpp>
#include <opencv2\imgproc\imgproc.hpp>

using namespace std;
using namespace cv;
/*���Ա任*/
int main()
{
	Mat srcImg = imread("D:/Pic/simple/amazed.png", 0);
	if (!srcImg.data)
	{
		cout << "����ͼƬʧ��" << endl;
		return -1;
	}
	double k, b;
	cout << "������k��bֵ��";
	cin >> k >> b;
	int RowsNum = srcImg.rows;
	int ColsNum = srcImg.cols;
	Mat dstImg(srcImg.size(), srcImg.type());
	//���б���ͼ������,��ÿ�����ؽ�����Ӧ�����Ա任
	for (int i = 0; i < srcImg.rows; i++)
	{
		uchar *srcData = srcImg.ptr<uchar>(i);
		for (int j = 0; j < srcImg.cols; j++)
		{
			dstImg.at<uchar>(i, j) = srcData[j] * k + b;
		}
	}
	imshow("ԭͼ", srcImg);
	imshow("���Ա任���ͼ��", dstImg);
	waitKey();
	return 0;
}