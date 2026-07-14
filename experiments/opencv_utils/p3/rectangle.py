import cv2

img = cv2.imread("C:\\Users\\princ\\OneDrive\\Desktop\\New folder\\p3\\a12.jpg")

if img is None:
    print("not found")      
else:
    print("load img")

    p1 = (300, 100)
    p2 = (800, 1000)        
    color = (0, 255, 0)
    thickness = 5
    rectangle_img = cv2.rectangle(img, p1, p2, color, thickness)
    
    cv2.imshow("rectangle",rectangle_img)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()