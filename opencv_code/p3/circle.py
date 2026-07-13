import cv2

img = cv2.imread("C:\\Users\\princ\\OneDrive\\Desktop\\New folder\\p3\\a12.jpg")

if img is None:
    print("not found")      
else:
    print("load img")

    
    circle = cv2.circle(img, (500, 500), 300, (0, 255, 0), 5)
    
    cv2.imshow("circle",circle)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()