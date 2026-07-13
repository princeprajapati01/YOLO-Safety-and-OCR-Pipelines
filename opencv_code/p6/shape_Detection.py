import cv2
import numpy as np

# ==========================================
# READ IMAGE
# ==========================================

image_name = input("Enter image name with extension: ")

img = cv2.imread(image_name)

if img is None:
    print("Image not found!")
    exit()

# Resize image for better viewing
img = cv2.resize(img, (800, 600))

# Copy of original image
output = img.copy()

# ==========================================
# PREPROCESSING
# ==========================================

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur image to remove noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Threshold
_, thresh = cv2.threshold(
    blur,
    240,
    255,
    cv2.THRESH_BINARY_INV
)

# ==========================================
# FIND CONTOURS
# ==========================================

contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# ==========================================
# FUNCTION TO DETECT SHAPE
# ==========================================

def detect_shape(contour):

    # Area
    area = cv2.contourArea(contour)

    # Ignore very small shapes
    if area < 500:
        return "Noise"

    # Perimeter
    perimeter = cv2.arcLength(contour, True)

    # Approximate contour
    approx = cv2.approxPolyDP(
        contour,
        0.02 * perimeter,
        True
    )

    corners = len(approx)

    # ======================================
    # TRIANGLE
    # ======================================

    if corners == 3:
        return "Triangle"

    # ======================================
    # RECTANGLE / SQUARE
    # ======================================

    elif corners == 4:

        x, y, w, h = cv2.boundingRect(approx)

        aspect_ratio = w / float(h)

        # Square
        if 0.95 <= aspect_ratio <= 1.05:
            return "Square"

        # Rectangle
        else:
            return "Rectangle"

    # ======================================
    # PENTAGON
    # ======================================

    elif corners == 5:
        return "Pentagon"

    # ======================================
    # HEXAGON
    # ======================================

    elif corners == 6:
        return "Hexagon"

    # ======================================
    # CIRCLE / OVAL
    # ======================================

    else:

        circularity = (
            4 * np.pi * area
        ) / (perimeter * perimeter)

        # Circle
        if circularity > 0.80:
            return "Circle"

        # Oval
        else:
            return "Oval"

# ==========================================
# DRAW RESULTS
# ==========================================

for contour in contours:

    shape = detect_shape(contour)

    if shape == "Noise":
        continue

    # Draw contour
    cv2.drawContours(
        output,
        [contour],
        -1,
        (0, 255, 0),
        3
    )

    # Find center point
    M = cv2.moments(contour)

    if M["m00"] != 0:

        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])

    else:
        cx, cy = 0, 0

    # Put shape name
    cv2.putText(
        output,
        shape,
        (cx - 40, cy),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

# ==========================================
# SHOW IMAGES
# ==========================================

cv2.imshow("Original Image", img)

cv2.imshow("Threshold Image", thresh)

cv2.imshow("Detected Shapes", output)

# ==========================================
# WAIT & CLOSE
# ==========================================

cv2.waitKey(0)

cv2.destroyAllWindows()
