import cv2

img = cv2.imread(r"C:\Users\princ\OneDrive\Desktop\New folder\p4\flower.webp")

blur = cv2.GaussianBlur(img,(7,7),0)

cv2.imshow("original img",img)

cv2.imshow("blur img",blur)

#save the blur image
cv2.imwrite(r"C:\Users\princ\OneDrive\Desktop\New folder\p4\flower_blur.webp",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()