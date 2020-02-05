# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:55:06 2020

@author: User
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg', 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # 隐藏x、y轴
plt.show()
helpimread = help(cv2.imread)
print(helpimread)

