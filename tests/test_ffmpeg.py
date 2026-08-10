from pathlib import Path
import time
from src.core.ffmpeg_recorder import FFmpegRecorder


output_path = Path("teste_ffmpeg.mp4")

recorder = FFmpegRecorder(output_path)

print("Iniciando...")
recorder.start()

print("Gravando por 10 segundos...")

time.sleep(10)

recorder.stop()

print("Fim.")