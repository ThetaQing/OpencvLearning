# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 19:47:16 2020
Introduction：从视频文件中读取并显示帧
@author: User
"""

import numpy as np
import cv2
 
cap = cv2.VideoCapture('haer.mp4')
# 定义多媒体数字信息编解码器，创建VideoWriter对象
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # 翻转
        frame = cv2.flip(frame, 0)
        # 写入翻转后的帧
        out.write(frame)
        
        
        cv2.imshow('frame', frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):  # 可控制捕获帧的速度
            break
        
    else:
        break
# 释放 
cap.release()
out.release()
cv2.destroyAllWindows()