import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread(r"C:\Users\reddy\OneDrive\Desktop\Screenshot 2026-02-03 142138.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)

# Display original image
plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

# Display edge detected image
plt.subplot(1,2,2)
plt.title("Canny Edge Detection")
plt.imshow(edges, cmap="gray")
plt.axis("off")

plt.show()
