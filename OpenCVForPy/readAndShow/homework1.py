# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:08:07 2020

@author: User
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg')
# 用cv2加载的彩色图片，编码方式是BGR

# cv2可以正常显示
cv2.imshow('image',img)
'''
# 如果需要用cv2显示的话取消注释
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()
'''    
# matplotlib显示不正常，编码方式是RGB     
plt.imshow(img, interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # 隐藏x、y轴
plt.show()
'''
# 如果需要查看帮助文档的话取消注释
docPltImshow = help(plt.imshow)
print(docPltImshow)  # 打印plt模块下的imshow函数的帮助文档
'''


