from pathlib import Path
import subprocess


FFMPEG_PATH = Path(
    r"C:\Users\HENRI\Downloads"
    r"\ffmpeg-9.0-essentials_build"
    r"\ffmpeg-9.0-essentials_build"
    r"\bin"
    r"\ffmpeg.exe"
)


class FFmpegRecorder:

    def __init__(self, output_path):

        self.output_path = output_path
        self.process = None

    def start(self):

        command = [
            str(FFMPEG_PATH),

            "-y",

            "-f",
            "dshow",

            "-video_size",
            "1920x1080",

            "-framerate",
            "30",

            "-rtbufsize",
            "512M",

            "-i",
            "video=DroidCam Video",

            # Segmentação
            "-f",
            "segment",

            "-segment_time",
            "5",

            "-reset_timestamps",
            "1",

            "-c:v",
            "h264_qsv",

            "-global_quality",
            "20",

            "-pix_fmt",
            "nv12",

            "-movflags",
            "+faststart",

            str(self.output_path / "segment_%03d.mp4"),
        ]

        print("Comando FFmpeg:")
        print(" ".join(map(str, command)))

        self.output_path.mkdir(parents=True, exist_ok=True)

        self.process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
        )

    def stop(self):

        if self.process:

            print("Parando gravação...")

            self.process.stdin.write(b"q")
            self.process.stdin.flush()

            self.process.wait()

            print("Gravação finalizada.")

            self.process = None