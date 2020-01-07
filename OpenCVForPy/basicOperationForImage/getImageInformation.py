# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:14:04 2020
Introduction：获取图像属性
@author: User
"""

import cv2
import numpy as np
img = cv2.imread('D:/picture/amazing/6.png')
 
 # 获取图像形状,如果是灰度图仅返回行数和列数，彩色图还有通道数
print(img.shape)
 # 返回图像的像素数目
print(img.size)
 # 返回图像的数据类型
print(img.dtype)