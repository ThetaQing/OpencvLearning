# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:21:29 2020
Introduction：图像的ROI
@author: User
"""

import cv2
import numpy as np
img = cv2.imread('D:/picture/amazing/6.png')
print(img.shape)
# 取出感兴趣的ROI
region = img[100:400, 100:400]
# 对该ROI进行处理，在这里，我们将img[400:700, 400:700]的部分用ROI重置
img[400:700, 400:700] = region
# 显示
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()
    