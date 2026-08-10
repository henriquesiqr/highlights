from pathlib import Path
from .ffmpeg_recorder import FFmpegRecorder


class GameRecorder:

    def __init__(
        self,
        output_path: str,
        width: int,
        height: int,
        fps: int,
        codec: str,
    ):

        self.output_path = Path(output_path)

        self.width = width
        self.height = height
        self.fps = fps
        self.codec = codec

        self.recorder = FFmpegRecorder(self.output_path)

        self.is_recording = False

    def start(self):

        print(
            f"Iniciando gravação: "
            f"{self.width}x{self.height} @ {self.fps} FPS"
        )

        self.recorder.start()

        self.is_recording = True

    def write(self, frame):

        # O FFmpeg captura diretamente da DroidCam.
        pass

    def stop(self):

        if self.is_recording:

            self.recorder.stop()

            self.is_recording = False