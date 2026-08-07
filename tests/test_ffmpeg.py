import time
from pathlib import Path
import sys

sys.path.append(
    str(Path(__file__).resolve().parents[1] / "src")
)

from core.ffmpeg_recorder import FFmpegRecorder


recorder = FFmpegRecorder("teste.mp4")

print("Iniciando...")

recorder.start()

time.sleep(10)

print("Parando...")

recorder.stop()

print("Fim.")