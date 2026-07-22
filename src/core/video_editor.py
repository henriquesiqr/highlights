from pathlib import Path
from moviepy import VideoFileClip
from core.highlight import Highlight
 
 
class VideoEditor:
 
    def export(
        self,
        input_video: str,
        output_dir: str,
        highlight: Highlight,
    ):
 
        output_path = (
            Path(output_dir)
            / f"highlight_{highlight.id:03d}.mp4"
        )
 
        clip = VideoFileClip(input_video)
        
        start = max(0, highlight.start)
        end = min(highlight.end, clip.duration)
        
        if start >= end:
            print(f"Highlight {highlight.id} ignorado.")
            clip.close()
            return
        highlight_clip = clip.subclipped(start, end)
 
        highlight_clip.write_videofile(
            str(output_path),
            codec="libx264",
            audio=False,
            logger=None,
        )
 
        highlight_clip.close()
        clip.close()
 
        print(f"Exportado: {output_path.name}")