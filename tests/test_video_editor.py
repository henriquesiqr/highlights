from core.video_editor import VideoEditor
from core.highlight import Highlight
 
 
editor = VideoEditor()
 
highlight = Highlight(
    id=1,
    start=5,
    end=15,
)
 
editor.export(
    input_video="recordings/game_temp.mp4",
    output_dir="highlights",
    highlight=highlight,
)
 
print("Highlight exportado!")