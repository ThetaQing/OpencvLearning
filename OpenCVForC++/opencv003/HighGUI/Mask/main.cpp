#include "mask.h"
#include <opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>  
#include<opencv2/imgproc/imgproc.hpp>  
#include <iostream>  

using namespace cv;
using namespace std;
int main() {
	Mat src = imread("suidao.png");
	if (src.empty())
	{
		return-1;
	}

	Mat BGR[3];
	split(src, BGR);
	BGR[0] = mask(BGR[0]);
	BGR[1] = mask(BGR[1]);
	BGR[2] = mask(BGR[2]);
	Mat maskBGR;
	merge(BGR, 3, maskBGR);
	maskBGR = maskBGR(Rect(0, 0, src.size().width, src.size().height));
	cout << maskBGR.size() << maskBGR.type();
	cout << src.size() << src.type();
	src.convertTo(src, maskBGR.type(), 1 / 255.0);
	imshow("maskBGR", maskBGR);
	
	maskBGR = src - maskBGR + 20.0 / 255.0;
	namedWindow("InputImage");
	imshow("InputImage", src);
	imshow("RESULT", maskBGR);
	

	waitKey();
	return 0;
}