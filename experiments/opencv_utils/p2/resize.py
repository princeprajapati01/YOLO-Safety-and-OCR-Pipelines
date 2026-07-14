import cv2

img = cv2.imread("C:\\Users\\princ\\OneDrive\\Desktop\\New folder\\p2\\img.jpg")

if img is None:
    print("not found")
else:
    print("load img")

    resize = cv2.resize(img , (200,150))
#                                w   h
    cv2.imshow("original",img)
    cv2.imshow("Resize img",resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("resizeimg.jpg",resize)
