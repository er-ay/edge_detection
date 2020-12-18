# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 01:50:56 2020

@author: Ayse
"""

import cv2 

video = cv2.VideoCapture(r'...video.mp4')


result = cv2.VideoWriter('vid.avi',  
            cv2.VideoWriter_fourcc(*'DIVX'), 
            20, (640,640), 0) 

while True:

    ret, frame = video.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    edges = cv2.Canny(gray, 45, 90)

    result.write(edges)
        
    #cv2.imshow("result", edges)

    key = cv2.waitKey(1) 
    if key == ord("q"): 
        break
      

result.release()
video.release()
cv2.destroyAllWindows() 

