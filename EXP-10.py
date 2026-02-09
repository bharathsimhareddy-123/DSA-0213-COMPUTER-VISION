import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\reddy\OneDrive\Desktop\COMPUTER VISION\iii.jpg")

h, w = img.shape[:2]

# Source points (from original image)
src_pts = np.float32([
    [50, 50],
    [300, 50],
    [50, 300],
    [300, 300]
])

# Destination points
dst_pts = np.float32([
    [0, 0],
    [w, 0],
    [0, h],
    [w, h]
])

# Find homography matrix
H, status = cv2.findHomography(src_pts, dst_pts)

# Apply homography transformation
homography_img = cv2.warpPerspective(img, H, (w, h))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformed Image", homography_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
