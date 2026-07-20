from pathlib import Path
from src.core.video_editor import VideoEditor

editor = VideoEditor()

editor.export(
    input_video="recordings/game_temp.mp4",
    output_video="highlights/teste.mp4",
    start=5,
    end=15,
)

print("Highlight exportado com sucesso!")