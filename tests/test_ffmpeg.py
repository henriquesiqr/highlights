from pathlib import Path
import time

from src.core.ffmpeg_recorder import FFmpegRecorder


output_path = Path("teste_segmentos")


recorder = FFmpegRecorder(output_path)


print("Iniciando...")

recorder.start()

print("Gravando por 20 segundos...")

time.sleep(20)

recorder.stop()

print("Fim.")