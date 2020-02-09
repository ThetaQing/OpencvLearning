# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 13:00:31 2020

@author: Administrator
"""

import cv2
filename = 'big.jpg'
def detect(filename):
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    
    img = cv2.imread(filename)
    # 人脸检测需要灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 开始人脸检测，传递的参数是scaleFactor和minNeighbors，分别表示人脸检测过程中每次迭代时图像的压缩率以及每个人脸矩形
    # 保留近邻数目的最小值。
    # 检测操作的返回值为人脸矩形数组
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for(x, y, w, h) in faces:
        # cv2.rectangle允许通过坐标来绘制矩形(x, y)表示左上角的坐标， (w, h)表示人脸矩形的宽度和高度
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.namedWindow('Vikings Detected!!!')
    cv2.imshow('Vikings Detected!!!', img)
    cv2.imwrite('viking.jpg', img)
    cv2.waitKey(0)
    
detect(filename)