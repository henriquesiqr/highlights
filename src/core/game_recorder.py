import cv2


class GameRecorder:

    def __init__(
        self,
        output_path: str,
        width: int,
        height: int,
        fps: int,
        codec: str,
    ):

        self.output_path = output_path
        self.width = width
        self.height = height
        self.fps = fps
        self.codec = codec

        self.writer = None
        self.is_recording = False

    def start(self):

        fourcc = cv2.VideoWriter_fourcc(*self.codec)

        self.writer = cv2.VideoWriter(
            self.output_path,
            fourcc,
            self.fps,
            (self.width, self.height),
        )

        self.is_recording = True

    def write(self, frame):

        if self.is_recording:
            self.writer.write(frame)

    def stop(self):

        if self.writer is not None:
            self.writer.release()

        self.is_recording = False