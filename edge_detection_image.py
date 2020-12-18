# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 03:12:48 2020

@author: Ayse
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\\Users\\User\\Desktop\\flowers\\cicek.jpeg',0)
edges = cv2.Canny(img,25,90)

genislik = int(img.shape[1])
yukseklik = int(img.shape[0])
dim = (genislik,yukseklik)

edges = cv2.resize(edges,dim)

plt.imshow(edges, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

cv2.imshow("a",edges)
cv2.waitKey(10000)