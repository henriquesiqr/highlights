import json
import sys
from pathlib import Path

from core.highlight import Highlight
from core.video_editor import VideoEditor
from core.config import native_video_basename


def find_video(session_folder: Path) -> Path | None:

    matches = list(session_folder.glob(f"{native_video_basename}.*"))

    return matches[0] if matches else None


def main():

    if len(sys.argv) < 2:
        print("Uso: python src/export.py <pasta_da_sessao>")
        return

    session_folder = Path(sys.argv[1])

    highlights_path = session_folder / "highlights.json"

    if not highlights_path.exists():
        print(f"Arquivo não encontrado: {highlights_path}")
        return

    video_path = find_video(session_folder)

    if video_path is None:
        print(
            f"Nenhum vídeo '{native_video_basename}.*' encontrado em "
            f"{session_folder}. Transfira o vídeo do iPhone antes de exportar."
        )
        return

    with open(highlights_path) as f:
        raw_highlights = json.load(f)

    highlights = [Highlight(**h) for h in raw_highlights]

    editor = VideoEditor()

    print(f"Exportando {len(highlights)} highlights de {video_path.name}...\n")

    for highlight in highlights:
        editor.export(
            video_path=str(video_path),
            output_dir=str(session_folder),
            highlight=highlight,
        )

    print("\nExportação concluída.")


if __name__ == "__main__":
    main()