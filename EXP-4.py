import cv2

# Read image
img = cv2.imread(r"C:\Users\reddy\OneDrive\Desktop\COMPUTER VISION\Screenshot 2026-02-03 141851.png")

# Check if image is loaded
if img is None:
    print("Image not found")
    exit()

# Bigger image (Zoom In)
bigger = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# Smaller image (Zoom Out)
smaller = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()
