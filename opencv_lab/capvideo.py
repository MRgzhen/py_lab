import cv2

fourcc = cv2.VideoWriter_fourcc(*"MJPG")
out = cv2.VideoWriter("./out.avi", fourcc, 25.0, (640, 480))

cv2.namedWindow("view", cv2.WINDOW_NORMAL)
cv2.resizeWindow("view", 640, 360)

# 获取视频设备（cv2.VideoCapture("/home/gz/video.mp4")）
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # 从摄像头读取视频
    ret, frame = cap.read()

    if ret == True:
        # 将视频帧显示在窗口中
        cv2.imshow("video", frame)

        # 将视频帧写入输出文件
        out.write(frame)

        # 等待按键事件
        key = cv2.waitKey(1)
        if (key & 0xFF) == ord("q"):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
