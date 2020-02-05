# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:01:51 2020

@author: Administrator

Introduction:视频读取
"""
import cv2

videoCapture = cv2.VideoCapture('D:/movies/haer.mp4')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWiter = cv2.VideoWriter('MyOutput.avi', cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)
# 未压缩的YUV颜色编码
success, frame = videoCapture.read()
while success:
    videoWiter.write(frame)
    success, frame = videoCapture.read()
