import subprocess
from pathlib import Path

from core.config import ffmpeg_path
from core.highlight import Highlight


class VideoEditor:

    def export(
        self,
        video_path: str,
        output_dir: str,
        highlight: Highlight,
    ):

        output_path = Path(output_dir) / f"highlight_{highlight.id:03d}.mp4"

        start = max(0, highlight.start)
        duration = highlight.end - highlight.start

        command = [
            str(ffmpeg_path),
            "-y",
            "-hide_banner",
            "-loglevel", "warning",
            "-nostats",
            "-ss", f"{start:.3f}",
            "-i", str(video_path),
            "-t", f"{duration:.3f}",
            "-c", "copy",
            str(output_path),
        ]

        subprocess.run(command, check=True)

        print(f"Exportado: {output_path.name}")