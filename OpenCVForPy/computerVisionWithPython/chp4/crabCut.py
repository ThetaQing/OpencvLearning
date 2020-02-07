# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 17:27:08 2020

@author: Administrator
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

# 首先加载想要处理的图像
img = cv2.imread('statue_small.jpg')
# 创建一个与所加载图像同形状的掩模，并用0填充
mask = np.zeros(img.shape[:2],np.uint8)

# 创建以0填充的前景和背景模型
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# 用一个标识出想要隔离的对象的矩形来初始化GrabCut算法
rect = (110, 50, 400, 350)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * mask2[:, :, np.newaxis]

plt.subplot(121), plt.imshow(img)
plt.title("grabcut"), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(cv2.imread('statue_small.jpg'), cv2.COLOR_BGR2RGB))
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.show()