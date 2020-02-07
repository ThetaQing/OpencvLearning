import cv2
import numpy as np

img = np.zeros((200, 200), dtype=np.uint8) # 创建一个200*200的黑色空白图像
img[50:150, 50:150] = 255 # 图像中央放置白色方块

ret, thresh = cv2.threshold(img, 127, 255, 0) # 二值化操作 
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # 轮廓查找
# 参数：输入图像、层次类型核轮廓逼近方法
# 函数返回值： 修改后的图像、图像的轮廓以及它们的层次
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) # 颜色空间转换
img = cv2.drawContours(color, contours, -1, (0,255,0), 2) # 使用轮廓来画出图像的彩色版本
cv2.imshow("contours", color) # 得到一个边缘为绿色的白色方块
cv2.waitKey()
cv2.destroyAllWindows()

