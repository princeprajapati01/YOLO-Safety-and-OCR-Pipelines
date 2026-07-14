import cv2

user = input("enter a location: ")

img = cv2.imread(user)

while True:
    print("1. line drawing")
    print("2. circle drawing")
    print("3. rectangle drawing")
    print("4. text drawing ")
    print("5. exit")

    choice = int(input("enter your choice: "))
    if choice == 1:
        x1 = int(input("enter x1: "))
        y1 = int(input("enter y1: "))
        x2 = int(input("enter x2: "))
        y2 = int(input("enter y2: "))
        color = (0, 255, 0)
        thickness = 5
        cv2.line(img, (x1, y1), (x2, y2), color, thickness)
        

    elif choice == 2:
        x = int(input("enter x: "))
        y = int(input("enter y: "))
        radius = int(input("enter radius: "))
        color = (0, 255, 0)
        thickness = 5
        cv2.circle(img, (x, y), radius, color, thickness)

    elif choice == 3:
        x1 = int(input("enter x1: "))
        y1 = int(input("enter y1: "))
        x2 = int(input("enter x2: "))
        y2 = int(input("enter y2: "))
        color = (0, 255, 0)
        thickness = 5
        cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)        

    elif choice == 4:
        x = int(input("enter x: "))
        y = int(input("enter y: "))
        text = input("enter text: ")
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (0, 255, 0)
        thickness = 2
        cv2.putText(img, text, (x, y), font, fontScale, color, thickness)

    elif choice == 5:
        break

    else:
        print("invalid choice")
    
    save = input("do you want to save the image? (y/n): ")
    if save == 'y':
        cv2.imwrite("output.jpg", img)
        print("image saved as output.jpg")
        break
    elif save == 'n':
        continue
    else:
        print("invalid input")
    
