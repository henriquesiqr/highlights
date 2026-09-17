from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Vídeo nativo do iPhone (transferido manualmente após a partida)
# Aceita qualquer extensão (game.mp4, game.mov, etc.) — ver export.py
native_video_basename = "game"

# Highlights
buffer_seconds = 20

# ffmpeg (usado só na etapa de exportação/corte)
ffmpeg_path = PROJECT_ROOT / "tools" / "ffmpeg" / "bin" / "ffmpeg.exe"

if not ffmpeg_path.exists():
    raise FileNotFoundError(
        f"ffmpeg.exe não encontrado em {ffmpeg_path}. "
        "Baixe o ffmpeg e coloque o executável nesse caminho (veja o README)."
    )

# Teclado
key_start = "n"
key_highlight = "h"
key_end = "f"
key_exit = "esc"