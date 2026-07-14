import cv2
from xgboost import cv

img = cv2.imread("C:\\Users\\princ\\OneDrive\\Desktop\\New folder\\p2\\img.jpg")

if img is None:
    print("img not")
else:
    flip_hori = cv2.flip(img,1)
    flip_verti = cv2.flip(img,0)
    flip_both = cv2.flip(img,-1)
    cv2.imshow("original",img)
    cv2.imshow("flip_hori",flip_hori)
    cv2.imshow("flip_verti",flip_verti)
    cv2.imshow("flip_both",flip_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()