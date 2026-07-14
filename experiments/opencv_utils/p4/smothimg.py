import cv2

img = cv2.imread(r"C:\Users\princ\OneDrive\Desktop\New folder\p4\flower_blur.webp")

clen = cv2.medianBlur(img,3)

cv2.imshow("orignal ",img)
cv2.imshow("clen",clen)

cv2.waitKey(0)
cv2.destroyAllWindows()