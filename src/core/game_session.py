import cv2
from pathlib import Path
from core.camera import Camera
from core.game_recorder import GameRecorder
from core.highlight_manager import HighlightManager
from core.video_editor import VideoEditor
from core.config import (
    frame_width,
    frame_height,
    fps,
    video_codec,
    recordings_dir,
    temp_video_name,
    window_name,
)


class GameSession:

    def __init__(self):

        self.output_path = Path(recordings_dir) / temp_video_name

        self.camera = Camera()

        self.recorder = GameRecorder(
            output_path=str(self.output_path),
            width=frame_width,
            height=frame_height,
            fps=fps,
            codec=video_codec,
        )

        self.highlight_manager = HighlightManager()

        self.video_editor = VideoEditor()

    def run(self):

        self.recorder.start()

        while True:

            ret, frame = self.camera.read()

            if not ret:
                print("Erro ao capturar frame.")
                break

            self.recorder.write(frame)

            cv2.imshow(window_name, frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("h"):
                self.highlight_manager.add_highlight()
            elif key == 27:
                break

        self.recorder.stop()
        for highlight in self.highlight_manager.highlights:
            self.video_editor.export(
                input_video=str(self.output_path),
                output_dir="highlights",
                highlight=highlight,
            )
        self.camera.release()
        cv2.destroyAllWindows()

        print("\nHighlights registrados:")
        for i, highlight in enumerate(self.highlight_manager.highlights, start=1):
            print(
                f"{i:02d}. "
                f"{highlight.start:.2f}s → "
                f"{highlight.end:.2f}s"
            )
        print("Gravação finalizada.")