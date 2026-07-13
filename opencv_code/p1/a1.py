import cv2

# Prompt user for image filename
file_input = input("Enter image filename (with extension): ")
IMG = cv2.imread(file_input)

if IMG is None:
	print("Error: Image not found or path is incorrect.")
else:
	gray = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)
	cv2.imshow('gray img', gray)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	# Prompt user for save location
	save_path = input("Enter filename (with path) to save the image: ")
	cv2.imwrite(save_path, IMG)
	print(f"Image saved to {save_path}")