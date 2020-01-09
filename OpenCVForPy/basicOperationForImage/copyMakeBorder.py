# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:56:14 2020
Introduction：边界填充的几种方法
@author: User
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [0,0,255]

img1 = cv2.imread('D:/picture/amazing/6.png')
img1 = img1[:,:,::-1]
# 分别表示上、下、左、右填充的像素数
replicate = cv2.copyMakeBorder(img1, 100,100,100,100, cv2.BORDER_REPLICATE) # 复制最后一个像素
reflect = cv2.copyMakeBorder(img1, 100, 100, 100, 100, cv2.BORDER_REFLECT) # 镜像abcg|gcda
reflect101 = cv2.copyMakeBorder(img1, 100, 100, 100, 100, cv2.BORDER_REFLECT_101) # 镜像abcd|cba
wrap = cv2.copyMakeBorder(img1, 100, 100, 100, 100, cv2.BORDER_WRAP) # 缠绕
constant = cv2.copyMakeBorder(img1, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value = BLUE) # 常数填充

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()