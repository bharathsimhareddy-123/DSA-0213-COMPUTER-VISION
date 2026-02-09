import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\reddy\OneDrive\Desktop\Screenshot 2026-02-03 141858.png")

blur = cv2.GaussianBlur(img, (5, 5), 0)

plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Gaussian Blur")
plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.show()
