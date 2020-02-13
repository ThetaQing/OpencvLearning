# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:54:18 2020

@author: Administrator
"""

import cv2
import numpy as np

img = cv2.imread('chess_board.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度图
gray = np.float32(gray)

# 调用cornerHarris函数，最重要的是第三个参数，该参数限定了Sobel算子的中孔。
# Sobel算子通过对图像行、列的变化检测来检测边缘，Sobel算子
# 会通过核来完成检测。简单地说，该参数定义了角点检测地敏感度，
# 其取值必须是介于3核31之间的奇数。如果参数设为3，当检测到方块的边界时，
# 棋盘中黑色方块的所有对角线都会被认为是角点。如果参数设置为23
# 只有每个方块的角点才会才会被检测为角点。

# 第二个参数可以改变这种情况，即参数值越小，标记角点的记号越小。

dst = cv2.cornerHarris(gray, 2, 11, 0.04)
img[dst > 0.01 * dst.max()] = [0, 0, 255]

while(True):
    cv2.imshow('corners', img)
    if cv2.waitKey(10) & 0xff == ord("q"):
        break
cv2.destroyAllWindows()

