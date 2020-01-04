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

# Image spatial resolution change
resolved_img = np.zeros((int(img.shape[0]/3), int(img.shape[1]/3)))
resolved_img.shape
for i in range(0, img.shape[0] -1):
    for j in range(0, img.shape[1] - 1):
        resolved_img[int(i/3), int(j/3)] = np.sum(img[i:i+3, j:j+3])
plt.imshow(resolved_img,cmap='gray',interpolation='bicubic')

resolved_img2 = np.zeros((int(img2.shape[0]/3), int(img2.shape[1]/3)))
resolved_img2.shape
for i in range(0, img2.shape[0] -1):
    for j in range(0, img2.shape[1] - 1):
        resolved_img2[int(i/3), int(j/3)] = np.sum(img[i:i+3, j:j+3])
plt.imshow(resolved_img2,cmap='gray',interpolation='bicubic')

plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
r = 100.0 / img3.shape[1]
dim = (100, int(img3.shape[0] * r))

resized = cv2.resize(img3, dim, interpolation = cv2.INTER_AREA)
plt.imshow(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))
