# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:06:40 2020
Introduction: FourCC是一个4字节码，用来确定视频的编码格式。
@author: User
"""
import numpy as np
import cv2
# 如果是从文件中读取，只需要更改端口0为视频文件名即可
cap = cv2.VideoCapture(0)
# Window下的编码器为DIVX
fourcc = cv2.VideoWriter_fourcc(*'DIVX') 
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        frame = cv2.flip(frame, 0)
        
        out.write(frame)
        
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("None Image")
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()