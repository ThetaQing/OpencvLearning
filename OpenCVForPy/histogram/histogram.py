# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 09:43:43 2020
Introduction：直方图的计算，绘制与分析
@author: User
"""

import numpy as np
import cv2

img = cv2.imread('test.png', 0)
clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8, 8))

cl1 = clahe.apply(img)

cv2.imwrite('equTest.png', cl1)
