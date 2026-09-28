import cv2
import numpy as np

# 视频https://www.bilibili.com/video/BV1M7oMYXE5h/?spm_id_from=333.788.player.switch&vd_source=c83b07b6a1d88d9707e8970e33bedbe2&p=16
# 视频https://www.bilibili.com/video/BV11341127pe/?spm_id_from=333.337.search-card.all.click&vd_source=c83b07b6a1d88d9707e8970e33bedbe2
# ========== 读取 1.webm → 缩放 → 转灰度显示 → 另存为 2.avi ==========#
# cap = cv2.VideoCapture('1.webm')
# fps = 10.0
# fourcc = cv2.VideoWriter_fourcc(*"MJPG")
# out = cv2.VideoWriter("./2.avi", fourcc, fps, (640, 400))

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:          # 视频结束或读取失败
#         break

#     frame = cv2.resize(frame, (640, 400))
#     newFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame', newFrame)
#     out.write(frame)

#     if (cv2.waitKey(5) & 0xFF) == ord("q"):
#         break

# cap.release()
# out.release()
# cv2.destroyAllWindows()


# ========== 2. ROI区域     读取 img.png → B/G 通道置零（只留红色）→ 显示 ==========#
# img = cv2.imread("./img.png")   # 读入图像（路径错误时返回 None，不报错）
# img_copy = img.copy()           # 复制一份，避免修改原图
# img_copy[:, :, 0] = 0           # B 通道置 0（OpenCV 通道顺序是 BGR）
# img_copy[:, :, 1] = 0           # G 通道置 0
# cv2.imshow("img", img_copy)     # 窗口显示图像
# cv2.waitKey(0)                  # 等待按键（缺少这行窗口会一闪而过，看不到显示）
# cv2.destroyAllWindows()         # 关闭所有窗口


# ========== 3. 边界填充 ==========#
# - BORDER_REPLICATE：复制法，也就是复制最边缘像素。
# - BORDER_REFLECT：反射法，对感兴趣的图像中的像素在两边进行复制例如: fedcba|abcdefgh|hgfedcb
# - BORDER_REFLECT_101：反射法，也就是以最边缘像素为轴，对称，gfedcb|abcdefgh|gfedcba
# - BORDER_WRAP：外包装法 cdefgh|abcdefgh|abcdefg
# - BORDER_CONSTANT：常量法，常数值填充。
# img = cv2.imread("./img.png")
# top_size, bottom_size, left_size, right_size = (50, 50, 50, 50)
# replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)
# constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_CONSTANT, value=0)
# cv2.imshow('img3', constant)
# cv2.waitKey()
# cv2.destroyAllWindows()


# ========== 4. 数值计算 ==========#
# ========== 4.1 数值计算 ==========#
# img = cv2.imread('./img.png')
# img_new = img + 10
# img_new2 = cv2.add(img, img_new)
# cv2.imshow('img4', img_new)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ========== 4.2 数值计算---图像融合 ==============#
# cat = cv2.imread("./img.png")
# dog = cv2.imread("./dog.png")
# print(cat.shape)
# print(dog.shape)
# dog = cv2.resize(dog, (1119, 1019))
# # dog = cv2.resize(dog, (0,0), fx=3, fy=3) # 同比例缩放
# print(dog.shape)
# res = cv2.addWeighted(cat, 0.4, dog, 0.6, 0)
# cv2.imshow("img5", res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ========== 5. 形态学 ==============#
# ========== 5.1 腐蚀性操作 ==============#
# img = cv2.imread("./erode.png")
# if img is None:
#     raise FileNotFoundError("图像读取失败，检查路径")
# kernel = np.ones((5, 5), dtype=np.uint8)
# erosion = cv2.erode(img, kernel)
# cv2.imshow("img5", erosion)
# cv2.imshow("img6", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ========== 5.2 膨胀性操作 ==============#
# img = cv2.imread("./erode.png")
# if img is None:
#     raise FileNotFoundError("图像读取失败，检查路径")
# kernel = np.ones((5, 5), dtype=np.uint8)
# dige = cv2.dilate(img, kernel)
# cv2.imshow("img5", img)
# cv2.imshow("img6", dige)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ========== 5.3 开运算与闭运算 ==============#
# 开运算：先腐蚀后膨胀
# 闭运算：先膨胀后腐蚀
# img = cv2.imread("./erode.png")
# if img is None:
#     raise FileNotFoundError("图像读取失败，检查路径")
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# cv2.imshow("img5", img)
# cv2.imshow("img6", open)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread("./erode.png")
# if img is None:
#     raise FileNotFoundError("图像读取失败，检查路径")
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("img5", img)
# cv2.imshow("img6", close)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ========== 5.4 梯度运算 ==============#
# 梯度 == 膨胀图像 - 腐蚀图像

# 方式一
# img = cv2.imread("./circle.png")
# if img is None:
#     raise FileNotFoundError("图像读取失败，检查路径")
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# erosion = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# cv2.imshow("img5", img)
# cv2.imshow("img6", erosion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 方式二
# img = cv2.imread("./circle.png")
# if img is None:
#     raise FileNotFoundError("图像读取失败，检查路径")
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# dilate = cv2.dilate(img, kernel)
# erosion = cv2.erode(img, kernel)
# res = cv2.subtract(dilate, erosion)
# cv2.imshow("img5", dilate)
# cv2.imshow("img7", erosion)
# cv2.imshow("img6", res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ========== 5.5 礼貌&黑帽 ==============#
# 礼貌：原图 - 开运算
# img = cv2.imread("./erode.png")
# if img is None:
#     raise FileNotFoundError("图像读取失败，检查路径")
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# cv2.imshow("img5", tophat)
# cv2.imshow("img6", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 黑帽：闭运算 - 原图
# img = cv2.imread("./erode.png")
# if img is None:
#     raise FileNotFoundError("图像读取失败，检查路径")
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# tophat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
# cv2.imshow("img5", tophat)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ========== 6 梯度 ==============#
# img = cv2.imread("./dog.png")
# if img is None:
#     raise FileNotFoundError("图像读取失败，检查路径")
# sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
# sobelx = cv2.convertScaleAbs(sobelx)

# sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
# sobely = cv2.convertScaleAbs(sobely)

# sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
# cv2.imshow("img5", sobel)
# cv2.imshow("img6", sobelx)
# cv2.imshow("img7", sobely)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ========== 7 阈值 ==============#
# ret, dst = cv2.threshold(src, thresh, maxval, type)
# - src: 输入图，只能输入单通道图像，通常来说为灰度图
# - dst: 输出图
# - thresh: 阈值
# - maxval: 当像素值超过了阈值（或者小于阈值，根据type来决定），所赋予的值
# - type: 二值化操作的类型，包含以下5种类型： cv2.THRESH_BINARY; cv2.THRESH_BINARY_INV; cv2.THRESH_TRUNC; cv2.THRESH_TOZERO; cv2.THRESH_TOZERO_INV
# - cv2.THRESH_BINARY 超过阈值部分取maxval（最大值），否则取0
# - cv2.THRESH_BINARY_INV THRESH_BINARY的反转
# - cv2.THRESH_TRUNC 大于阈值部分设为阈值，否则不变
# - cv2.THRESH_TOZERO 大于阈值部分不改变，否则设为0
# - cv2.THRESH_TOZERO_INV THRESH_TOZERO的反转

# img = cv2.imread("./dog.png")
# if img is None:
#     raise FileNotFoundError("图像读取失败，检查路径")
# ret, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow("img5", threshold)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ========== 8 图像平滑 ==============#
# 均值滤波
# img = cv2.imread("./blur.png")
# if img is None:
#     raise FileNotFoundError("图像读取失败，检查路径")
# blur = cv2.blur(img, (3, 3))
# cv2.imshow("img5", blur)
# cv2.imshow("img6", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 方框滤波
# img = cv2.imread("./blur.png")
# if img is None:
#     raise FileNotFoundError("图像读取失败，检查路径")
# blur = cv2.boxFilter(img, -1, (3, 3), normalize=True)
# cv2.imshow("img5", blur)
# cv2.imshow("img6", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ========== 9 Canny边缘检测 ==============#
# img = cv2.imread("./dog.png")
# if img is None:
#     raise FileNotFoundError("图像读取失败，检查路径")
# canny = cv2.Canny(img, 30, 100)
# cv2.imshow("img5", canny)
# cv2.imshow("img6", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ========== 10 图像金字塔 ==============#


# ========== 11 轮廓检测 ==============#
# - **RETR_EXTERNAL**：只检索最外面的轮廓；
# - **RETR_LIST**：检索所有的轮廓，并将其保存到一条链表当中；
# - **RETR_CCOMP**：检索所有的轮廓，并将他们组织为两层：顶层是各部分的外部边界，第二层是空洞的边界；
# - **RETR_TREE**：检索所有的轮廓，并重构嵌套轮廓的整个层次；

# # method（轮廓逼近方法）

# - **CHAIN_APPROX_NONE**：以 Freeman 链码的方式输出轮廓，所有其他方法输出多边形（顶点的序列）。
# - **CHAIN_APPROX_SIMPLE**：压缩水平的、垂直的和斜的部分，也就是，函数只保留他们的终点部分。
# img = cv2.imread("./contours.png")
# if img is None:
#     raise FileNotFoundError("图像读取失败，检查路径")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# # 绘制轮廓
# draw_img = img.copy()
# res = cv2.drawContours(draw_img, contours, -1, (0, 0, 255), 2)
# # 轮廓特征
# cnt = max(contours, key=cv2.contourArea)
# area = cv2.contourArea(cnt)
# arcLength = cv2.arcLength(cnt, True)
# print(f"area: {area}, arcLength: {arcLength}")
# # 轮廓近似
# epsilon = 0.01 * arcLength
# approx = cv2.approxPolyDP(cnt, epsilon, True)
# draw_approx = img.copy()
# res2 = cv2.drawContours(draw_approx, [approx], -1, (0, 255, 0), 2)  # 绿色画近似轮廓

# # cv2.imshow("img5", img)
# # cv2.imshow("img6", thresh)
# # cv2.imshow("img7", res)
# cv2.imshow("img8", res2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ========== 12 模板匹配 ==============#
