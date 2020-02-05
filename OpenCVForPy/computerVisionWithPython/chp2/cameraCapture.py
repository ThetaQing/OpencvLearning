# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:33:14 2020

@author: Administrator
"""

import cv2

cameraCapture = cv2.VideoCapture(0)
fps = 30 # an assumption
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWiter = cv2.VideoWriter('MyOutput.avi', cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)
success, frame = cameraCapture.read()
numFramesRemaining = 10 * fps - 1
while success and numFramesRemaining > 0:
    videoWiter.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1
cameraCapture.release()