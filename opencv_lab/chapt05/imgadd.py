import cv2
import numpy as np

dog = cv2.imread("./img.png")

print(dog.shape)

img = np.ones((1019, 1119, 3), np.uint8) * 100

result = cv2.add(dog, img)

cv2.imshow('img', dog)
cv2.imshow('img2', result)
cv2.waitKey(0)

