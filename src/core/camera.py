from core.config import camera_source
import cv2

class Camera:

    def __init__(self):
        self.cap = cv2.VideoCapture(camera_source)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        self.cap.set(cv2.CAP_PROP_FPS, 60)

    def read(self):
        return self.cap.read()

    def release(self):
        self.cap.release()