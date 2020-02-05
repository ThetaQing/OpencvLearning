#include <opencv2/opencv.hpp>
#include <iostream> 
# include "highgui.hpp"
using namespace cv;
using namespace std;

int equalizeHist();
int equalizeHist_Color();


int main()
{
	equalizeHist();
	equalizeHist_Color();
	waitKey(0);
	return 0;
}

int equalizeHist()
{
	std::string strPath = "D:/Pic/simple/";
	Mat matSrc = imread(strPath + "amazed.png");
	if (matSrc.empty())
	{
		return -1;
	}
	imshow("src", matSrc);
	Mat matGray;
	cvtColor(matSrc, matGray, CV_BGR2GRAY);
	// 直方图均衡化
	Mat matResult;
	equalizeHist(matGray, matResult);

	imshow("equlizeHist", matResult);
	imwrite(strPath + "pic2_gray.jpg", matGray);
	imwrite(strPath + "pic2_equlizeHist.jpg", matResult);
	return 0;
}

int equalizeHist_Color()
{
	std::string strPath = "D:/Pic/simple/";
	Mat matSrc = imread(strPath + "amazed.png");
	if (matSrc.empty())
	{
		return -1;
	}
	Mat matArray[3];
	split(matSrc, matArray);
	// 直方图均衡化
	for (int i = 0; i < 3; i++)
	{
		equalizeHist(matArray[i], matArray[i]);
	}
	Mat matResult;
	merge(matArray, 3, matResult);


	imshow("src", matSrc);
	imshow("equlizeHist", matResult);

	imwrite(strPath + "pic2_equlizeHist_color.jpg", matResult);
	return 0;
}

