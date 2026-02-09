import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\reddy\OneDrive\Desktop\Screenshot 2026-02-06 122628.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to binary image
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply dilation
dilated = cv2.dilate(binary, kernel, iterations=1)

# Display original image
plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(gray, cmap="gray")
plt.axis("off")

# Display dilated image
plt.subplot(1,2,2)
plt.title("Dilated Image")
plt.imshow(dilated, cmap="gray")
plt.axis("off")

plt.show()
