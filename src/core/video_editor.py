import subprocess
from pathlib import Path

from core.config import ffmpeg_path, segment_time
from core.highlight import Highlight


class VideoEditor:

    def export(
        self,
        segments_dir: str,
        output_dir: str,
        highlight: Highlight,
    ):

        segments_dir = Path(segments_dir)
        output_dir = Path(output_dir)

        segments = sorted(segments_dir.glob("segment_*.mp4"))

        if not segments:
            print(f"Highlight {highlight.id}: nenhum segmento encontrado.")
            return

        idx_start = max(0, int(highlight.start // segment_time))
        idx_end = min(len(segments) - 1, int(highlight.end // segment_time))

        if idx_start > idx_end:
            print(f"Highlight {highlight.id} ignorado (fora do intervalo).")
            return

        selected = segments[idx_start:idx_end + 1]

        concat_list = segments_dir / f"_concat_{highlight.id:03d}.txt"
        concat_video = segments_dir / f"_concat_{highlight.id:03d}.mp4"

        with open(concat_list, "w") as f:
            for segment in selected:
                f.write(f"file '{segment.resolve()}'\n")

        subprocess.run(
            [
                str(ffmpeg_path), "-y",
                "-f", "concat", "-safe", "0",
                "-i", str(concat_list),
                "-c", "copy",
                str(concat_video),
            ],
            check=True,
        )

        offset = highlight.start - (idx_start * segment_time)
        duration = highlight.end - highlight.start

        output_path = output_dir / f"highlight_{highlight.id:03d}.mp4"

        subprocess.run(
            [
                str(ffmpeg_path), "-y",
                "-ss", f"{offset:.3f}",
                "-i", str(concat_video),
                "-t", f"{duration:.3f}",
                "-c:v", "libx264",
                "-preset", "veryfast",
                "-an",
                str(output_path),
            ],
            check=True,
        )

        concat_list.unlink()
        concat_video.unlink()

        print(f"Exportado: {output_path.name}")