# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:12:52 2020

@author: Administrator
"""
import cv2
import numpy as np


# 读取图片，第二个参数为False时，显示为灰度图像，True为原图，路径中不能包含中文，\有效
img = cv2.imread(filename="Mean_05_63.jpg",flags=True)
# 显示图片，第一个参数为窗口的标题，第二个参数为需要显示的图片
cv2.imshow(winname = "JPG", mat = img)
# 等待图片关闭，不写这句图片会一闪而过甚至死机，中间设置参数为多少毫秒后自动关闭
cv2.waitKey()
# 保存图片
cv2.imwrite("new.jpg",img)
# 创建一个窗口，第一个参数为窗口的唯一标识，第二个参数为窗口属性
# 窗口创建时可以添加的属性：

# cv2.WINDOW_NORMAL：窗口大小可以改变（同cv2.WINDOW_GUI_NORMAL）
# cv2.WINDOW_AUTOSIZE：窗口大小不能改变
# cv2.WINDOW_FREERATIO：窗口大小自适应比例
# cv2.WINDOW_KEEPRATIO：窗口大小保持比例
# cv2.WINDOW_GUI_EXPANDED：显示色彩变成暗色
# cv2.WINDOW_FULLSCREEN：全屏显示
# cv2.WINDOW_OPENGL：支持OpenGL的窗口

cv2.namedWindow(winname="win1", flags=cv2.WINDOW_NORMAL)
# 图片显示在上面创建的窗口，保持winname一致
cv2.imshow(winname = "win1", mat=img)
# 图片常用属性
# 打印图片高、宽和通道数
print(img.shape)
# 打印图片的像素数目
print(img.size)
# 打印图片的格式
print(img.dtype)
cv2.waitKey(5000)


# 泛洪填充
def fill_color_demo():
    copyImg = img.copy()
    h, w = img.shape[:2]
    # 生成一个大小为(h+2,w+2)颜色通道为1的图片
    mask = np.zeros([h+2, w+2], np.uint8)
    # 泛红填充
    # floodFill(image, mask, seedPoint, newVal, loDiff=None, upDiff=None,flags=None)
    # image为原图像，mask为掩码，单通道8位图像，比image的高度多2个像素，宽度多2个像素；
    # seedPoint：起始点（原像素点，相当于喷枪时鼠标点击的那个像素点）
    # newVal：在重绘区域像素的新值（RBG值）
    # loDiff：像素值的下限差值（最多比原像素点低多少）
    # upDiff：像素值的上限差值（最多比原像素点高多少）
    # flags：属性，FLOODFILL_FIXED_RANGE表示改变图像，泛洪填充，FLOODFILL_MASK_ONLY表示不改变图像，只填充遮罩层本身，忽略新的颜色值参数
    cv2.floodFill(copyImg, mask, (100,200), (0, 255, 0), (100,100,100),(50,50,50),cv2.FLOODFILL_FIXED_RANGE)
    cv2.imshow(winname="win1", mat=copyImg)
    cv2.waitKey(5000)

fill_color_demo()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
meanImg = cv2.medianBlur(gray,13)
grad_x = cv2.Scharr(meanImg, cv2.CV_32F,1,0)
grad_y = cv2.Scharr(meanImg, cv2.CV_32F,0,1)
gradx = cv2.convertScaleAbs(grad_x) # 取绝对值
grady = cv2.convertScaleAbs(grad_y)
# 计算两个图像的权值和
sobelImg = cv2.addWeighted(gradx, 0.5, grady, 0.5, 0)
cv2.imshow(winname="win1",mat= sobelImg)
cv2.waitKey(5000)
cv2.imshow(winname="win1", mat = grad_x)
cv2.waitKey(5000)
cv2.imshow(winname="win1",mat=grad_y)
cv2.waitKey(5000)
lapImg = cv2.Laplacian(meanImg,cv2.CV_32F)
# lapImg = cv2.convertScaleAbs(lapImg)
cv2.imshow(winname="win1",mat=lapImg)
cv2.waitKey(5000)
# threshold阈值分割的类型是uint8
ret, binary = cv2.threshold(sobelImg, 100,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
cv2.imshow(winname="win1", mat=binary)
cv2.waitKey(5000)
#OpenCV定义的结构元素  
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))

erodeImg = cv2.erode(binary, kernel)
cv2.imshow(winname="win1", mat=erodeImg)
cv2.waitKey(5000)

print(lapImg.dtype)
print(sobelImg.dtype)
# 销毁窗口
cv2.destroyWindow("win1")

