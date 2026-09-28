import cv2
import numpy as np

img = cv2.imread("/home/gz/图片/img.png")

# shape属性中包含三个信息
# 高度、长度、通道数
print(img.shape)

#   图像占用多大空间
# 高度 * 长度 * 通道数
print(img.size)

# 图像中每个元素的位深
print(img.byteswap)
