# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:32:42 2020
Introduction：图像的基本操作
    1、获取像素值并修改
    2、获取图像的属性（行、列、通道、图像数据类型、像素数目等）
    3、图像的ROI()
    4、图像通道的拆分与合并
@author: User
"""
import cv2
import numpy as np
# 读取一幅图像
img = cv2.imread('D:/picture/amazing/6.png')
# 通过行列坐标获取该点的像素值
px = img[100,100]
print(px)
# OpenCV中的排序是BGR，所以第0个通道是blue分量
bule = img[100, 100, 0]
print(bule)

# 修改像素值
img[100,100] = [255, 255, 255]
print (img[100,100])

'''
Tips:Numpy是优化了的快速矩阵运算软件包，不推荐逐个获取像素值进行修改，能用矩阵运算不用循环
'''
# 另一种获取和修改像素值更好的方法
print(img.item(10,10,2))
img.itemset((10,10,2), 100)
print(img.item(10,10,2))

helpItem = help(img.item)
print(helpItem)