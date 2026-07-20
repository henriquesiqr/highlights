import cv2
from pathlib import Path
from core.camera import Camera
from core.game_recorder import GameRecorder
from core.config import (
    frame_width,
    frame_height,
    fps,
    video_codec,
    recordings_dir,
    temp_video_name,
    window_name,
)

# Cria o caminho do arquivo temporário
output_path = Path(recordings_dir) / temp_video_name

# Inicializa câmera
camera = Camera()

# Inicializa gravador
recorder = GameRecorder(
    output_path=str(output_path),
    width=frame_width,
    height=frame_height,
    fps=fps,
    codec=video_codec,
)

recorder.start()

while True:

    ret, frame = camera.read()

    if not ret:
        print("Erro ao capturar frame.")
        break

    recorder.write(frame)

    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) == 27:  # ESC
        break

recorder.stop()
camera.release()
cv2.destroyAllWindows()

print("Gravação finalizada.")