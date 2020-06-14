import cv2
cam= cv2.VideoCapture(0)
while(True):
    val,img=cam.read()
    cv2.startWindowThread()
    cv2.namedWindow("abc")
    cv2.imshow("abc",img)
    cv2.waitKey()
cam.release()
