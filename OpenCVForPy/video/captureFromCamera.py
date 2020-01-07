# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 19:06:38 2020
Introduction:
        1、读取视频文件，显示视频，保存视频文件
        2、从摄像头获取并显示视频
@author: User
"""
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # 逐帧捕获图像
    
    ret, frame = cap.read()
    # 对捕获的图像进行灰度处理，如果注释掉显示的就是彩色图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 对处理后的图像显示
    cv2.imshow('frame', frame)
    
    # 按键结束，q表示退出捕获
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# 退出之后停止捕获并关闭窗口
cap.release()
cv2.destroyAllWindows()
