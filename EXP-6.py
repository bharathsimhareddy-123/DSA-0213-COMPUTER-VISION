import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\reddy\OneDrive\Desktop\COMPUTER VISION\iii.jpg")

# Get image size
rows, cols = img.shape[:2]

# Translation values
tx = 100   # move right by 100 pixels
ty = 50    # move down by 50 pixels

# Translation matrix
M = np.float32([[1, 0, tx],
                [0, 1, ty]])

# Apply translation
moved = cv2.warpAffine(img, M, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Moved Image", moved)

cv2.waitKey(0)
cv2.destroyAllWindows()
