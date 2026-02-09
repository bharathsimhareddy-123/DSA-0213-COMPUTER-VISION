import cv2

# Read image
img = cv2.imread(r"C:\Users\reddy\OneDrive\Desktop\COMPUTER VISION\iii.jpg")

# Get image size
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

# Clockwise rotation (45 degrees)
rot_clock = cv2.getRotationMatrix2D(center, -45, 1.0)
clockwise = cv2.warpAffine(img, rot_clock, (w, h))

# Counter-clockwise rotation (45 degrees)
rot_counter = cv2.getRotationMatrix2D(center, 45, 1.0)
counterclockwise = cv2.warpAffine(img, rot_counter, (w, h))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Clockwise Rotation", clockwise)
cv2.imshow("Counter-Clockwise Rotation", counterclockwise)

cv2.waitKey(0)
cv2.destroyAllWindows()
