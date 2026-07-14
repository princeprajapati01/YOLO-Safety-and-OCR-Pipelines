import cv2
import numpy as np

img = cv2.imread(r"C:\Users\princ\OneDrive\Desktop\New folder\p4\lowresolasion.jpg")

sharpen_kernal = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

sharpen_kernal = cv2.filter2D(img,-1,sharpen_kernal)

cv2.imshow("orignal img",img)
cv2.imshow("final output img ", sharpen_kernal)

cv2.waitKey(0)
cv2.destroyAllWindows()