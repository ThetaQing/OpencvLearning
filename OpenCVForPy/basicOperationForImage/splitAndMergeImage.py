# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:49:58 2020

@author: User
"""

import cv2
import numpy as ny
img = cv2.imread('D:/picture/amazing/6.png')
# 拆分通道，注意，该过程很耗时，只有真正需要的时候才用
b, g, r = cv2.split(img)
img = cv2.merge([b, g, r])
# 显示
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('raw.png', img)
    cv2.destroyAllWindows()
    
# 如果令红色通道为0
img[:, :, 2] = 0
# 或者先拆分后赋值,只是慢一点
# b = img[:,:,0]
    # 显示
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('noneRed.png', img)
    cv2.destroyAllWindows()
    
    