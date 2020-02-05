# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:44:13 2020

@author: User
"""

import cv2
import numpy as np
'''
# 查询所有的颜色变换
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print (flags)
'''
# 获取RGB空间中的颜色在HSV空间中的值
green = np.uint8([[[0, 255, 0]]]) # 输入RGB排序的值，这里的三层括号应该分别对应于 cvArray， cvMat， IplImage
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsv_green)

cap = cv2.VideoCapture('F:/Code/opencv/OpenCVCode/OpencvLearning/OpenCVForPy/video/haer.mp4')

while(1):
    # 获取每一帧
    ret, frame = cap.read()
    if ret == True:
        # 转换到HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # 设定指定颜色的阈值，对应HSV的颜色分量
        lower_green = np.array([40,110, 110]) # ([110, 50, 50]) # 蓝色
        upper_green = np.array([70, 255, 255]) # ([130,255,255])
        
        # 根据阈值构建掩模
        mask = cv2.inRange(hsv, lower_green, upper_green)
        
        # 对原图像和掩模进行位运算
        res = cv2.bitwise_and(frame, frame, mask = mask)
        
        # 显示图像
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    else:
        print('None Image')
        break

# 关闭窗口
cap.release()
cv2.destroyAllWindows()