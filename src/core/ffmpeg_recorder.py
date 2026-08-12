import subprocess
from pathlib import Path

from core.config import (
    ffmpeg_path,
    camera_device_name,
    capture_width,
    capture_height,
    capture_fps,
    segment_time,
    video_quality,
)


class FFmpegRecorder:

    def __init__(self, segments_dir: Path):
        self.segments_dir = Path(segments_dir)
        self.process = None

    def start(self):

        self.segments_dir.mkdir(parents=True, exist_ok=True)

        command = [
            str(ffmpeg_path),
            "-y",
            "-hide_banner",
            "-loglevel", "warning",
            "-nostats",
            "-f", "dshow",
            "-video_size", f"{capture_width}x{capture_height}",
            "-framerate", str(capture_fps),
            "-rtbufsize", "512M",
            "-i", f"video={camera_device_name}",
            "-f", "segment",
            "-segment_time", str(segment_time),
            "-reset_timestamps", "1",
            "-c:v", "h264_qsv",
            "-global_quality", str(video_quality),
            "-pix_fmt", "nv12",
            "-movflags", "+faststart",
            str(self.segments_dir / "segment_%03d.mp4"),
        ]

        print("Comando FFmpeg:")
        print(" ".join(map(str, command)))

        self.process = subprocess.Popen(command, stdin=subprocess.PIPE)

    def stop(self):

        if self.process:
            print("Parando gravação...")
            self.process.stdin.write(b"q")
            self.process.stdin.flush()
            self.process.wait()
            print("Gravação finalizada.")
            self.process = None