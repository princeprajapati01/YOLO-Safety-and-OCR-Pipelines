import cv2

img = cv2.imread(r"C:\Users\princ\OneDrive\Desktop\New folder\OIP.webp")

blur = cv2.GaussianBlur(img,(7,7),0)


cv2.imshow("origanlimg",img)
cv2.imshow("blur img",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
