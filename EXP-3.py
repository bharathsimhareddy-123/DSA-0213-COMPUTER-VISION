import cv2

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Webcam Video", frame)

    # Normal speed
    key = cv2.waitKey(30) & 0xFF

    # Slow motion
    if key == ord('s'):
        cv2.waitKey(100)

    # Fast motion
    elif key == ord('f'):
        cv2.waitKey(5)

    # Exit
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
