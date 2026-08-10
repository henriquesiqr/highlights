from pathlib import Path
from .ffmpeg_recorder import FFmpegRecorder


class GameRecorder:

    def __init__(self, segments_dir: str):
        self.segments_dir = Path(segments_dir)
        self.recorder = FFmpegRecorder(self.segments_dir)
        self.is_recording = False

    def start(self):
        print("Iniciando gravação...")
        self.recorder.start()
        self.is_recording = True

    def stop(self):
        if self.is_recording:
            self.recorder.stop()
            self.is_recording = False