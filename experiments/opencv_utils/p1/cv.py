import cv2

img = cv2.imread('img.jpg')


#cv2.imshow('IMAAGE',img)  #open the window
#cv2.waitKey(0) # time 
#cv2.destroyAllWindows() # past img are window are deleted


# save the file     
#cv2.imwrite("output.jpg",img)  
    
#dimensions 

#h,w,c = img.shape
#print(f"height{h}\n,width{w}\n,color{c}\n")


#gray scale conversion

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image ", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()