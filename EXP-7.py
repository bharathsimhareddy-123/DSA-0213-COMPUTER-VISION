import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\reddy\OneDrive\Desktop\COMPUTER VISION\iii.jpg")

rows, cols = img.shape[:2]

# Points from original image
pts1 = np.float32([[50, 50],
                   [200, 50],
                   [50, 200]])

# Points in transformed image
pts2 = np.float32([[10, 100],
                   [200, 50],
                   [100, 250]])

# Affine transformation matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply affine transformation
affine_img = cv2.warpAffine(img, M, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformed Image", affine_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
