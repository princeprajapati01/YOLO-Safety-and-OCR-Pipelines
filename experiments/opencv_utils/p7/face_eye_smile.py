import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
smile_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(gray,1.1,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w , y+h), (0,255,0),2)

        roi_gray = gray[y:y+h , x:x+w]

        roi_color = frame[y:y+h , x:x+w]

        eyes = eye_cascades.detectMultiScale(roi_gray,1.1,10)
        if len(eyes) > 0 :
            cv2.putText(frame,"Eyes detection",(x, y-30), cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)

        smile = smile_cascades.detectMultiScale(roi_gray,1.7,20)
        if len(smile) > 0 :
            cv2.putText(frame,"smile detection",(x, y - 10), cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)

    cv2.imshow("smart face detecation" , frame)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

    