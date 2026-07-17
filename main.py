import cv2
from camera import Camera


camera = Camera()

while True:
    ret, frame = camera.read()
    if not ret:
        break
    cv2.imshow("PingReplay", frame)
    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()