import cv2
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.png')

# Rotate the image
(h, w) = img.shape[:2]
center = (w / 2, h / 2)
print(h,w)

M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))

M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))
