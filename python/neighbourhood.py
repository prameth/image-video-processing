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

# Neighborhood
result = ndimage.generic_filter(img, np.nanmean, size=3, mode='constant', cval=np.NaN)
plt.imshow(result,cmap='gray',interpolation='bicubic')
result = ndimage.generic_filter(img2, np.nanmean, size=3, mode='constant', cval=np.NaN)
plt.imshow(result,cmap='gray',interpolation='bicubic')
