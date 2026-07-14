#user propapative appliacasion to video strem

import cv2

camera = cv2.VideoCapture(0)



while True:
    success,image = camera.read()

    if not success:
        break

    cv2.imshow("video",image)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break