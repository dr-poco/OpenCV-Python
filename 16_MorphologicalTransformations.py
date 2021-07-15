import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('smarties.png', 0)

_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(mask, kernel, iterations = 2)
erotion = cv2.erode(mask, kernel, iterations = 1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # erosin followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) # diation followed by erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel) # difference between dilation & erotion of an image
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel) # difference between image & opening of an image

titles = ['image', 'mask', 'dilation', 'erotion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erotion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()