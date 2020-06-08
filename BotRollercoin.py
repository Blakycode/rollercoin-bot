# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 19:09:32 2020

@author: Blackycode
"""

import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui as au

#codigo para posicion del mouse
"""
import pyautogui as au
import time
time.sleep(3)
au.position()
"""
def dibujar(mask,color):
  _,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
      cv2.CHAIN_APPROX_SIMPLE)
  for c in contornos:
    area = cv2.contourArea(c)
    if area > 1450 and area < 3000:
      M = cv2.moments(c)
      if (M["m00"]==0): M["m00"]=1
      x = 364+ int(M["m10"]/M["m00"])
      y = 281+int(M['m01']/M['m00'])
      au.click(x,y+40)
      nuevoContorno = cv2.convexHull(c)
      cv2.circle(frame00,(x,y),7,(0,255,0),-1)
      cv2.putText(frame00,'{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
      cv2.drawContours(frame00, [nuevoContorno], 0, color, 3)
        



btcBajo = np.array([0,0,0],np.uint8)
btcAlto = np.array([70,70,200],np.uint8)
#LTC
ltcBajo = np.array([15,100,20],np.uint8)
ltcAlto = np.array([60,255,255],np.uint8)
#Dash
dashBajo = np.array([100,200,20],np.uint8)
dashAlto = np.array([125,255,255],np.uint8)

#Doge
dogeBajo = np.array([15,93,20],np.uint8)
dogeAlto = np.array([35, 227,247],np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    
  
    frame2 = np.array(ImageGrab.grab(bbox=(364,281,1138,890)))
    
  
    frame = cv2.cvtColor(frame2,cv2.COLOR_RGB2HSV)
    #resh = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

    frame00 = cv2.cvtColor(frame2,cv2.COLOR_BGR2RGB)
    

    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    maskBtc  = cv2.inRange(frame,btcBajo,btcAlto)
    maskDash  = cv2.inRange(frame,dashBajo,dashAlto)
    maskLtc = cv2.inRange(frame,ltcBajo,ltcAlto)
    maskDoge = cv2.inRange(frame,dogeBajo,dogeAlto)
    
    dibujar(maskBtc,(0,255,255)) #OK ltc
    dibujar(maskDash,(0,255,255)) #OK dash
    #dibujar(maskLtc,(0,255,255))
    dibujar(maskDoge,(0,255,255)) #OK btc y doge
    cv2.imshow('frame',frame00)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break

cv2.destroyAllWindows()
