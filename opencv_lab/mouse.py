import cv2
import numpy as np

def mouse_callback(event, x, y, flags, param):
    print(f"Mouse event: {event}, Position: ({x}, {y}), Flags: {flags}, Param: {param}")    
    
mouse_callback(1, 100, 200, 0, None)  # Simulate a mouse event for testing

# 创建窗口
cv2.namedWindow("Mouse", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Mouse", 640, 480)

# 设置鼠标回调函数
cv2.setMouseCallback("Mouse", mouse_callback, "123")

# 显示窗口与背景
img = np.zeros((480, 640, 3), np.uint8)  # Create a black image for display
while True:
    cv2.imshow("Mouse", img)  # Display the black image for mouse interaction
    key = cv2.waitKey(1)
    if(key & 0xFF) == ord("q"):
        break

cv2.destroyAllWindows()