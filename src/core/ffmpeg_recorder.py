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
        self.output_path = str(output_path)
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
            "60",
 
            "-rtbufsize",
            "512M",
 
            "-i",
            'video=DroidCam Video',
 
            "-c:v",
            "h264_mf",
 
            "-preset",
            "veryfast",
 
            "-pix_fmt",
            "yuv420p",
 
            "-movflags",
            "+faststart",
 
            self.output_path,
        ]
 
        print("Comando FFmpeg:")
        print(" ".join(command))
 
        self.process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
 
    def stop(self):
 
        if self.process is None:
            return
 
        try:
            self.process.stdin.write(b"q\n")
            self.process.stdin.flush()
 
            self.process.wait(timeout=5)
 
        except subprocess.TimeoutExpired:
            print("FFmpeg não encerrou normalmente. Finalizando processo...")
            self.process.kill()
            self.process.wait()
 
        finally:
            self.process = None