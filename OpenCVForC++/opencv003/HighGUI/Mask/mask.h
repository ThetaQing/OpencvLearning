#ifndef __mask_
#define __mask_
#include <opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>  
#include<opencv2/imgproc/imgproc.hpp>  
#include <iostream>  

using namespace cv;
using namespace std;
Mat FFT(Mat& src_gray);
Mat getFFTresultImg(Mat& completeI, CvSize srcSize);
Mat mask(Mat& plane);

//计算高斯滤波系数矩阵
Mat clcGLPFMat(Mat& mat, int D0);
#endif // !__mask_
#pragma once
