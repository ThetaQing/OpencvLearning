#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;
# define WINDOW_NAME "线性混合示例"  // 

const int g_nMaxAlphaValue = 100;  // 
int g_nAlphaValueSlider;  // 
double g_dAlphaValue;  // 
double g_dBetaValue;  // 

//  
Mat g_srcImage1;
Mat g_srcImage2;
Mat g_srcImage3;

void on_Trackbar(int, void*)
{
	// 
	g_dAlphaValue = (double)g_nAlphaValueSlider / g_nMaxAlphaValue;
	// 
	g_dBetaValue = (1.0 - g_dAlphaValue);

	// 
	addWeighted(g_srcImage1, g_dAlphaValue, g_srcImage2, g_dBetaValue, 0.0, g_dstImage, -1);
	imshow(WINDOW_NAME, g_dstImage);

}

int main()
{
	g_scrImage1 = imread("nezha.jpg");

}