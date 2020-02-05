# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 12:42:57 2020
Cameo类提供两种方法启动应用程序
@author: Administrator
"""
import cv2
from managers import WindowManager, CaptureManager

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0),self._windowManager, True)
        
    def run(self):
        """Run the main loop"""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            
            # TODO:Filter the frame(Chapter 3)
            
            self._captureManager.exitFrame()
            self._windowManager.processEvents()
            
    def onKeypress(self, keycode):
        """
        Handle a keypress.
        
        space -> Take a screenshot(抓屏).
        tab -> Start/stop recording a screencast(截屏视频).
        escape -> Quit.
        
        """
        
        if keycode == 32: # space
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('sreencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # escape
                self._windowManager.destroyWindow()
                # 应该要添加一句释放摄像头
                self._captureManager._capture.release()
                

if __name__ == "__main__":
    Cameo().run()
