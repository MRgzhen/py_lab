import cv2

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
img = cv2.imread("/home/gz/图片/img.png", cv2.IMREAD_COLOR)

cv2.imshow("img", img)
key = cv2.waitKey(0)

if(key & 0xFF == ord('q')):
    cv2.destroyAllWindows()
elif(key & 0xFF == ord('s')):
    print(f"save img to /home/gz/图片/imgnew.png")
    cv2.imwrite("/home/gz/图片/imgnew.png", img)