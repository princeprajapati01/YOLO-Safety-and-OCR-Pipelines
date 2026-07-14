import cv2

img = cv2.imread("C:\\Users\\princ\\OneDrive\\Desktop\\New folder\\p2\\img.jpg")

if img is None:
    print("img not")
else:
    (h ,w) = img.shape[:2]
    
    center = (w//2 , h//2)
    M = cv2.getRotationMatrix2D(center,-90,1.0)
    rotated = cv2.warpAffine(img , M ,(w,h))

    cv2.imshow("orignal",img)
    cv2.imshow("rotation",rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
