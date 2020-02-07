import cv2
import numpy as np

img = cv2.pyrDown(cv2.imread("hammer.png", cv2.IMREAD_UNCHANGED))

ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY) , 127, 255, cv2.THRESH_BINARY)
image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
  # find bounding box coordinates 先计算一个简单的边界框
  x,y,w,h = cv2.boundingRect(c)
  
  # 画出这个边界框
  cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 1)

  # find minimum area 计算出包围目标的最小局限区域
  rect = cv2.minAreaRect(c)
  # OpenCV中没有能直接从轮廓中计算出最小矩形顶点的坐标，所以需要计算出最小矩形区域，然后计算这个矩形的顶点。
  # calculate coordinates of the minimum area rectangle
  box = cv2.boxPoints(rect)
  # normalize coordinates to integers 计算出来的顶点坐标是浮点型，但是所得i像素的坐标值是整数
  box = np.int0(box)
  # draw contours 画出这个矩形 第二个参数接收一个保存着轮廓的数组，从而可以在一次操作中绘制一系列的轮廓，因此如果只有一组点
  # 来表示多边形轮廓，就需要把这组点放到一个数组里；第三个参数是要指定绘制的轮廓数组的所有：-1表示绘制所有的轮廓，否则就只绘制
  # 指定的轮廓，大多数绘图函数把绘图的颜色和密度放在最后两个参数中。
  cv2.drawContours(img, [box], 0, (0,0, 255), 3)
  
  # calculate center and radius of minimum enclosing circle 最后检查的边界轮廓为最小闭圆
  (x,y),radius = cv2.minEnclosingCircle(c)  # 返回圆心坐标和半径
  # cast to integers
  center = (int(x),int(y))
  radius = int(radius)
  # draw the circle
  img = cv2.circle(img,center,radius,(0,255,0),2)

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imshow("contours", img)

cv2.waitKey()
cv2.destroyAllWindows()
