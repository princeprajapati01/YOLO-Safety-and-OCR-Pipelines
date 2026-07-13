import cv2

img = cv2.imread(r"C:\Users\princ\OneDrive\Desktop\New folder\a1img.jpg",cv2.IMREAD_GRAYSCALE)

ret , thres_img = cv2.threshold(img , 150 , 255 , cv2.THRESH_BINARY)

cv2.imshow("origanl",img)
cv2.imshow("final",thres_img)

cv2.waitKey(0)
cv2.destroyAllWindows()