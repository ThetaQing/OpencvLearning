# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 14:17:15 2020

@author: Administrator
"""
# 导入模块
import cv2

# 定义检测人脸的detect函数
def detect():
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')
    camera = cv2.VideoCapture(0)
    
    while(True):
         # 捕获帧
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 检测
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)
            
            roi_gray = gray[y:y+h, x:x+w]
            # 通过限制对眼睛搜索的最小尺寸为40*40像素，可以去掉所有的假阳性（随机阴影）
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, 0, (40, 40))
            
            # 为人脸矩形框创建一个相对应的感兴趣区域，并对该矩形做“眼睛检测”
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(img, (ex + ey, ey + ew),(ex, ey), (0, 255, 0), 2)
                
        cv2.imshow("camera", frame)
        if cv2.waitKey(10) & 0xff == ord("q"):
            break
        
    camera.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    detect()
       
