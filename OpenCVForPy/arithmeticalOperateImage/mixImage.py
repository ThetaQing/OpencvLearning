# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 11:18:43 2020
Introduction：图像的算术运算
@author: User
"""

import cv2
import numpy as np
img1=cv2.imread('D:/picture/wall/1.png')
img2=cv2.imread('D:/picture/wall/2.jpg')
# 0.7表示第一幅图像的占比，0.3第二幅图像占比
dst=cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindow()
