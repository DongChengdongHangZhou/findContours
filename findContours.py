import cv2
import numpy as np

def binarization(img):
    pass

path = ''
img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
img = binarization(img)
contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

area = []
# 找到最大的轮廓
for k in range(len(contours)):
    area.append(cv2.contourArea(contours[k]))
max_idx = np.argmax(np.array(area))

# 填充最大的轮廓
masked = cv2.drawContours(img, contours, max_idx, 128 , cv2.FILLED)

    