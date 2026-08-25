from pathlib import Path

# Câmera / captura / fps
camera_device_name = "DroidCam Video"
capture_width = 1920
capture_height = 1080
capture_fps = 30

# Gravação
segment_time = 5       # duração de cada segmento, em segundos
buffer_seconds = 20    # janela de highlight
video_quality = 20     # global_quality do h264_qsv (menor = melhor)

recordings_dir = "recordings"
segments_folder_name = "segments"

ffmpeg_path = Path(
    r"C:\Users\HENRI\Downloads"
    r"\ffmpeg-9.0-essentials_build"
    r"\ffmpeg-9.0-essentials_build"
    r"\bin"
    r"\ffmpeg.exe"
)

# Teclado
key_start = "n"
key_highlight = "h"
key_end = "f"
key_exit = "esc"