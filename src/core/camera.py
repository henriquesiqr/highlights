from core.config import camera_source
import cv2

class Camera:

    def __init__(self):
        self.cap = cv2.VideoCapture(camera_source)

    def read(self):
        return self.cap.read()

    def release(self):
        self.cap.release()