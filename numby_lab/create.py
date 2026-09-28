import numpy as np
import cv2

# --------------------创将-------------#
# 通过array创建矩阵
# a = np.array([1, 2, 3])
# print(a)

# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b)


# 通过zeros创建矩阵
# c = np.zeros((5, 4, 3), np.uint8)
# print(c)

# 通过full创建矩阵
# d = np.full((5, 4, 3), 255, np.uint8)
# print(d)

#  单元矩阵
# e = np.identity(4)
# print(e)

e = np.eye(5, 7, k=3)
print(e)


# ---------------赋值------------------#

# img = np.zeros((480, 640, 3), np.uint8)
# print(img[100, 100])

# count = 0
# while count < 200:
#     img[count, 100, 0] = 255
#     count += 1
# cv2.imshow("img", img)

# key = cv2.waitKey(0)
# if (key & 0xFF) == ord("q"):
#     cv2.destoryAllWindows()


# --------------获取子矩阵-------------------#
# img = np.zeros((480, 640, 3), np.uint8)
# print(img[100, 100])
# roi = img[100:400, 100:600]
# roi[:] = [0, 0, 255]
# roi[10:150, 10:510] = [0, 255, 0]

# cv2.imshow("img", roi)
# count = 0
# # while count < 200:
# #     img[count, 100, 0] = 255
# #     count += 1
# # cv2.imshow("img", img)

# key = cv2.waitKey(0)
# if (key & 0xFF) == ord("q"):
#     cv2.destoryAllWindows()

