#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;

int main()
{
	//  ¿ªÊ¼
	Mat Nezha = imread("Nezha.jpg");
	namedWindow("NeZha");  // 
	imshow("NeZha", Nezha);  // 
	Mat dragon_girl = imread("dragon_girl.jpg",199);  // 
	Mat logo = imread("logo.jpg");
	namedWindow("DragonGirl");
	imshow("DragonGirl", dragon_girl);
	namedWindow("Logo");
	imshow("Logo", logo);

	Mat imageROI;
	imageROI = Nezha(Rect(0, 200, logo.cols, logo.rows));
	addWeighted(imageROI, 0.5, logo, 0.3, 0., imageROI);

	namedWindow("Mixing");
	imshow("Mixing", Nezha);
	//
	imwrite("Mixing.jpg", Nezha);
	waitKey();
	return 0;
}
/*
int main()
{
	MixingImage();
	return 0;
}
*/