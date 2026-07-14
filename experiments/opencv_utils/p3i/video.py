import cv2

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()  #return = true / flase

    if not ret:
        print("cloud not read frame")
        break
    
    cv2.imshow("webcam",frame)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        print("quittingggggggggggggggggg")
        break

cap.release()
cv2.destroyAllWindows()