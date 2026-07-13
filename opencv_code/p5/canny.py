import cv2

img = cv2.imread(r"C:\Users\princ\OneDrive\Desktop\New folder\p4\flower.webp", cv2.IMREAD_GRAYSCALE)

canny = cv2.Canny(img,150,240)

cv2.imshow("origanl",img)
cv2.imshow("final",canny)


cv2.waitKey(0)
cv2.destroyAllWindows()

