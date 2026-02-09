import cv2
import matplotlib.pyplot as plt

# Read the color image
img = cv2.imread(r"C:\Users\reddy\OneDrive\Desktop\Screenshot 2026-02-03 141851.png")
# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display original image
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Display grayscale image
plt.subplot(1, 2, 2)
plt.title("Grayscale Image")
plt.imshow(gray_img, cmap='gray')
plt.axis('off')

plt.show()
