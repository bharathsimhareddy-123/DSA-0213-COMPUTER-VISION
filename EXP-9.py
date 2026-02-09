import cv2
import numpy as np

# Open video file
cap = cv2.VideoCapture(
    r"C:\Users\reddy\OneDrive\Desktop\COMPUTER VISION\WIN_20260209_13_38_13_Pro.mp4"
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    # Source points
    pts1 = np.float32([
        [60, 60],
        [w-60, 60],
        [60, h-60],
        [w-60, h-60]
    ])

    # Destination points
    pts2 = np.float32([
        [0, 0],
        [w, 0],
        [0, h],
        [w, h]
    ])

    # Perspective transformation matrix
    M = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply transformation
    transformed = cv2.warpPerspective(frame, M, (w, h))

    # Display video
    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", transformed)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
