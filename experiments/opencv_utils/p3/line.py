import cv2

img = cv2.imread("C:\\Users\\princ\\OneDrive\\Desktop\\New folder\\p3\\a12.jpg")   

if img is None:
    print("not found")
else:
    print("load img")

    pt1 = (800, 400)
    pt2 = (100, 400)        
    color = (0, 255, 0)
    thickness = 5
    line_img = cv2.line(img, pt1, pt2, color, thickness)
    
    cv2.imshow("line",line_img)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()