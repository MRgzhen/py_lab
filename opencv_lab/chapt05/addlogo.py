# 1. 引入一幅图片

# 2. 要有一个LOGO，需要自己创建

# 3. 计算图片在什么地方添加，在添加的地方变成黑色

# 4. 利用add，将logo与图片叠加在一起


import cv2
import numpy as np

# 导出图片
dog = cv2.imread(".img.png")

# 创建logo
logo = np.zeros((200, 200, 3), np.uint8)
mask = np.zeros((200, 200), np.uint8)

# 绘制logo
logo[20:120, 20:120] = [0, 0, 255]
logo[80:180, 80:180] = [0, 255, 0]

mask[20:120, 20:120] = 255
mask[80:180, 80:180] = 255

m = cv2.bitwise_not(mask)

cv2.imshow('mask', mask)
cv2.imshow('logo', logo)
cv2.waitKey(0)

