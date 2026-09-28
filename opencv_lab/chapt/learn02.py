import cv2

"""
使用OpenCV读取并显示视频文件
通过循环逐帧读取视频并显示，直到视频结束
"""
# 创建视频捕获对象，从指定文件路径读取视频
vc = cv2.VideoCapture("./1.webm")

# 当视频文件成功打开时，进入循环
while vc.isOpened():
    # 读取视频帧
    ret, img = vc.read()
    # 如果成功读取到帧
    if ret:
        # 将图像大小调整为640x480
        newImg = cv2.resize(img, (640, 480))
        # 显示处理后的图像
        cv2.imshow("Video", newImg)
        # 等待10毫秒，实现视频播放效果
        key = cv2.waitKey(10)
        if key & 0xFF == ord("q"):
            break
    else:
        break

vc.release()
cv2.destroyAllWindows()
