import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\reddy\OneDrive\Desktop\COMPUTER VISION\iii.jpg")

rows, cols = img.shape[:2]

# Points from original image
pts1 = np.float32([[50, 50],
                   [300, 50],
                   [50, 300],
                   [300, 300]])

# Points in transformed image
pts2 = np.float32([[0, 0],
                   [cols, 0],
                   [0, rows],
                   [cols, rows]])

# Perspective transformation matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
perspective_img = cv2.warpPerspective(img, M, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformed Image", perspective_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
