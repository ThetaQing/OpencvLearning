# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:04:33 2020

@author: User
"""
import cv2
import numpy as np
# 载入图片
img = cv2.imread('messi5.jpg', 0)
# 显示图片
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()
    
