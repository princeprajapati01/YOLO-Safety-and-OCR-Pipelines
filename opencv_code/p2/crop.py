import cv2

img = cv2.imread("C:\\Users\\princ\\OneDrive\\Desktop\\New folder\\p2\\img.jpg")

if img is not None:
    cropp = img[400:800, 150:350]

    cv2.imshow('orignal',img)
    cv2.imshow('corpp',cropp)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
