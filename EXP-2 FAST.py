#FAST MOTION 
import cv2

cap = cv2.VideoCapture(r"C:\Users\reddy\OneDrive\Desktop\WIN_20260209_13_38_13_Pro.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Fast Motion Video", frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

