from ultralytics import YOLO

yolo = YOLO("icon.pt", task="detect")
# 图片
result = yolo(source="iconimg.png", save=True)


# 电脑屏幕
# result = yolo(source="screen", save=True)

# 摄像头
# result = yolo(source=0, save=True)
