import time
from pathlib import Path
import shutil

from core.actions import Action
from core.game_recorder import GameRecorder
from core.highlight_manager import HighlightManager
from core.video_editor import VideoEditor
from core.session_manager import SessionManager
from core.input_controller import InputController
from core.config import segments_folder_name


class GameSession:

    def __init__(self):

        self.input_controller = InputController()

        self.recorder = None
        self.segments_dir = None

        self.highlight_manager = HighlightManager()
        self.video_editor = VideoEditor()
        self.session_manager = SessionManager()

        self.game_running = False

    def run(self):

        print("=" * 40)
        print("PingCam")
        print()
        print("[N] Nova partida")
        print("[ESC] Encerrar")
        print("=" * 40)

        while True:

            action = self.input_controller.get_action()

            if not self.game_running:

                if action == Action.START_GAME:
                    self.start_game()

                elif action == Action.EXIT:
                    self.shutdown()
                    break

                time.sleep(0.05)
                continue

            if action == Action.HIGHLIGHT:
                self.highlight_manager.add_highlight()

            elif action == Action.END_GAME:
                self.end_game()

            elif action == Action.EXIT:
                self.shutdown()
                break

            time.sleep(0.05)

    def _wait_for_first_segment(self, timeout=10):

        first_segment = self.segments_dir / "segment_000.mp4"
        started = time.time()

        while not first_segment.exists():

            if time.time() - started > timeout:
                raise RuntimeError(
                    "Timeout esperando o ffmpeg iniciar a gravação."
                )

            time.sleep(0.05)

    def start_game(self):

        self.session_manager = SessionManager()

        self.segments_dir = (
            self.session_manager.session_folder / segments_folder_name
        )

        self.recorder = GameRecorder(segments_dir=str(self.segments_dir))
        self.recorder.start()

        # dá um respiro pro ffmpeg inicializar o device
        # antes de começar a contar o tempo dos highlights
        self._wait_for_first_segment()

        self.highlight_manager = HighlightManager()
        self.game_running = True

        print("\nPartida iniciada!")

    def export_highlights(self):

        print("\nExportando highlights...")
        success = True

        for highlight in self.highlight_manager.highlights:
            try:
                print(f"Exportando highlight {highlight.id}...")
                self.video_editor.export(
                    segments_dir=str(self.segments_dir),
                    output_dir=str(self.session_manager.session_folder),
                    highlight=highlight,
                )
            except Exception as e:
                success = False
                print(f"Erro ao exportar highlight {highlight.id}: {e}")

        return success

    def shutdown(self):
        self.input_controller.close()
        print("Pingcam encerrada.")

    def end_game(self):

        self.recorder.stop()

        success = self.export_highlights()

        if success and self.segments_dir.exists():
            shutil.rmtree(self.segments_dir)
            print("Segmentos temporários removidos.")
        elif not success:
            print("Segmentos mantidos para recuperação.")

        print("\nHighlights registrados:")
        for i, h in enumerate(self.highlight_manager.highlights, start=1):
            print(f"{i:02d}. {h.start:.2f}s → {h.end:.2f}s")

        self.game_running = False

        print("\n=====================================")
        print("Sessão finalizada!")
        print()
        print(f"{len(self.highlight_manager.highlights)} highlights exportados.")
        print()
        print("Pasta da sessão:")
        print(self.session_manager.session_folder)
        print("=====================================")