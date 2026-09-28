import cv2

def callback(x):
    pass

cv2.namedWindow("Color", cv2.WINDOW_NORMAL)

img = cv2.imread("/home/gz/图片/img.png")

colorspaces = [cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2BGRA,
               cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV_FULL,
               cv2.COLOR_BGR2YUV]
cv2.createTrackbar("curcolor", "Color", 0, 
                   len(colorspaces) - 1, callback)

while True:
    index = cv2.getTrackbarPos("curcolor", "Color")
    
    # 颜色空间转换
    cvt_img = cv2.cvtColor(img, colorspaces[index])
    cv2.imshow("Color", cvt_img)
    
    key = cv2.waitKey(10)
    if (key & 0xFF) == ord('q'):
        break
    
cv2.destroyAllWindows()