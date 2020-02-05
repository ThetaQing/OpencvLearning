# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 10:39:39 2020
该文件包含了CaptureManager的实现
@author: Administrator
"""

import cv2
import numpy
import time

class CaptureManager(object):
    """
    提取视频流
    """
    def __init__(self, capture, previewWindowManager = None,
                 shouldMirrorPreview = False):
        self.previewWindowManager = previewWindowManager
        self.shouldMirrorPreview = shouldMirrorPreview
        
        # 大多数成员变量为非公有变量，这类变量名前会加一个下划线进行标识，这些非公有变量与当前帧的状态以及文件写入操作有关
        
        self._capture = capture
        self._channel = 0
        self._enteredFrame = False
        self._frame = None
        self._imageFilename = None
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None
        
        self._startTime = None
        self._framesElapsed = int(0)
        self._fpsEstimate = None
        
    @property
    def channel(self):
        return self._channel
    
    @property
    def channel(self, value):
        if self._channel != value:
            self._channel = value
            self._frame = None
            
    @property
    def frame(self):
        if self._enteredFrame and self._frame is None:
            _, self._frame = self._capture.retrieve()
        return self._frame
    @property
    def isWritingImage(self):
        return self._imageFilename is not None
    
    @property
    def isWritingVideo(self):
        return self._videoFilename is not None
    
    def enterFrame(self):
        """
        Capture the next frame, if any.
        只能获取一帧，而且会推迟从一个通道的获取，以便随后从变量frame中读取
        
        """
        # But first, check that any previous frame was exited.
        assert not self._enteredFrame, "Tips: previous enterFrame() had no matching exitFrame()."
        if self._capture is not None:
            self._enteredFrame = self._capture.grab()
            
    def exitFrame(self):
        """
        Draw to the window, Write to files. Release the
        frame.
        可以从当前通道获取图像、估计帧速率、通过窗口管理器（如果有的话）显示图像，执行暂停
        的请求，从而向文件中写入图像
        """
        # Check whether any grabbed frame is retrievable.
        # The getter may retrieve and cache the frame.
        if self.frame is None:
            self._enteredFrame = False
            return
        
        # Update the FPS estimate and related variables.
        if self._framesElapsed == 0:  # 如果帧的运行时间为0
            self._startTime = time.time()
        else:
            timeElapsed = time.time() - self._startTime  # 运行时间计算
            # 这里的逻辑有一丢丢乱
            self._fpsEstimate = self._framesElapsed / timeElapsed  # 估计帧速率
        self._framesElapsed += 1
        
        # Draw to the window, if any.
        if self.previewWindowManager is not None:
            if self.shouldMirrorPreview:
                mirroredFrame = numpy.fliplr(self._frame).copy()  # 左右反转
                self.previewWindowManager.show(mirroredFrame)
            else:
                self.previewWindowManager.show(self._frame)
                
        # Write to the image file, if any.
        if self.isWritingImage:
            cv2.imwrite(self._imageFilename, self._frame)
            self._imageFilename = None
            
        # Write to the video file, if any.
        self._writeVideoFrame()
        # Release the frame
        self._frame = None
        self._enteredFrame = False
        
    # 其他写入文件的方法
    def writeImage(self, filename):
        """Write the next exited frame to an image file. """
        self._imageFilename = filename
        
    def startWritingVideo(self, filename, encoding = cv2.VideoWriter_fourcc('I','4','2','0')):
        """Start writing exited frames to a video file."""
        self._videoFilename = filename
        self._videoEncoding = encoding
        
    def stoptWritingVideo(self):
        """Stop writing exited frames to a video file."""
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None
        
    def _writeVideoFrame(self):
        if not self.isWritingVideo:
            return
        if self._videoWriter is None:
            fps = self._capture.get(cv2.CAP_PROP_FPS)
            if fps == 0.0:
                # The capture's FPS is unknown so use an estimate.
                if self._framesElapsed < 20:
                    # Wait until more frames elapse so that the 
                    # estimate is more stable.
                    return
                else:
                    fps = self._fpsEstimate
            size = (int (self._capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                    int(self._capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            self._videoWriter = cv2.VideoWriter(self._videoFilename, self._videoEncoding, fps,size)
        self._videoWriter.write(self._frame)
            
            
            
class WindowManager(object):
    """用来抽象窗口和键盘"""
    def __init__(self, windowName, keypressCallback = None):
        self.keypressCallback = keypressCallback
        
        self._windowName = windowName
        self._isWindowCreated = False
        
    @property
    def isWindowCreated(self):
        return self._isWindowCreated
    
    def createWindow(self):
        cv2.namedWindow(self._windowName)
        self._isWindowCreated = True
        
    def show(self, frame):
        cv2.imshow(self._windowName, frame)
        
    def destroyWindow(self):
        cv2.destroyWindow(self._windowName)
        self._isWindowCreated = False
        
    def processEvents(self):
        keycode = cv2.waitKey(1)
        if self.keypressCallback is not None and keycode != -1:
            # Discard any non_ASCII info encoded by GTK.
            keycode &= 0xFF
            self.keypressCallback(keycode)
    # 以上实现仅能支持键盘事件，对于鼠标事件可以次u该WindowManager
            
            
            
            
            
            
            
            