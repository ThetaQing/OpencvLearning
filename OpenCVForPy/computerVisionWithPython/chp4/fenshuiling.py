# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:42:30 2020
分水岭算法实现对背景剪除
@author: Administrator
"""

import numpy as np
import cv2
import os
print (cv2.__file__)
print(os.path)

from matplotlib import pyplot as plt
img = cv2.imread('statue_small.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 将颜色转为灰度之后，可为图像设一个阈值，这个操作可将图像分为两部分：黑色部分和白色部分
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 通过morphologyEx变换来去除噪声数据，这是一种对图像进行膨胀之后再进行腐蚀的操作，它可以提取图像特征
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 2)

#对变换之后的图像进行膨胀操作，可以得到大部分都是背景的区域
sure_bg = cv2.dilate(opening, kernel, iterations = 3)

# 反之，可以通过distanceTransform来获取确定的前景区域
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

# 之后应用一个阈值来决定那些区域是前景
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

# 确定前景和背景中重合的部分
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# 给出一些确定的前景区域，其中一些节点会连接在一起，而另一些节点并没有连接在一起
ret, markers = cv2.connectedComponents(sure_fg)

# 在背景区域上加1，这会将unknown区域设为0
markers = markers + 1
markers[unknown==255] = 0

# 最后打开门，让水漫起来并把栅栏绘成红色
markers = cv2.watershed(img, markers)
img[markers == -1] = [255,0,0]
plt.imshow(img)
plt.show()

