import cv2
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.png',cv2.IMREAD_GRAYSCALE)
plt.imshow(img,cmap='gray',interpolation='bicubic')
print(img)
img2 = cv2.imread('rose.jpg',cv2.IMREAD_GRAYSCALE)
plt.imshow(img2,cmap='gray',interpolation='bicubic')
img3 = cv2.imread('lena.png')

# Reduce intensity from 256 to 2
for i in range(0,img.shape[0]-1):
    for j in range(0,img.shape[1]):
        if img[i,j] < 255/2:
            img[i,j] = 0
        else:
            img[i,j] = 255
for i in range(0,img2.shape[0]-1):
    for j in range(0,img2.shape[1]):
        if img2[i,j] < 255/2:
            img2[i,j] = 0
        else:
            img2[i,j] = 255
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.imshow(img2,cmap='gray',interpolation='bicubic')
