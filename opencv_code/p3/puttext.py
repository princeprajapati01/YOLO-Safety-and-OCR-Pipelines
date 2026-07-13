import cv2

img = cv2.imread("C:\\Users\\princ\\OneDrive\\Desktop\\New folder\\p3\\a12.jpg")


if img is None:
    print("not found")
else:
    print("load img")

    font = cv2.FONT_HERSHEY_SIMPLEX
    text_img = cv2.putText(img, "Name:Prince", (100, 500), font, 3, (0, 10, 0), 5)
    cv2.imshow("text",text_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()