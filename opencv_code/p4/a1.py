import cv2
import numpy as np

path = input("Enter the path of the image: ")
img = cv2.imread(path)

if img is None:
    print("Image not found")
    exit()

while True:

    print("\n1. Blur the image")
    print("2. Smooth the image")
    print("3. Sharpen the image")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        blur = cv2.GaussianBlur(img, (7,7), 0)

        cv2.imshow("Original", img)
        cv2.imshow("Final Output", blur)

    elif choice == 2:

        smooth = cv2.medianBlur(img, 5)

        cv2.imshow("Original", img)
        cv2.imshow("Final Output", smooth)

    elif choice == 3:

        sk = np.array([
            [0,-1,0],
            [-1,5,-1],
            [0,-1,0]
        ])

        sharp = cv2.filter2D(img, -1, sk)

        cv2.imshow("Original", img)
        cv2.imshow("Final Output", sharp)

    elif choice == 4:
        break

    else:
        print("Invalid choice")

    cv2.waitKey(0)

cv2.destroyAllWindows()