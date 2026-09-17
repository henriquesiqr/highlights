import json
import time
from dataclasses import asdict

from core.actions import Action
from core.highlight_manager import HighlightManager
from core.session_manager import SessionManager
from core.input_controller import InputController
from core.config import native_video_basename


class GameSession:

    def __init__(self):

        self.input_controller = InputController()

        self.highlight_manager = HighlightManager()
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

    def start_game(self):

        self.session_manager = SessionManager()
        self.highlight_manager = HighlightManager()

        self.game_running = True

        print("\nPartida iniciada! Aperte REC no iPhone agora, se ainda não apertou.")

    def shutdown(self):
        self.input_controller.close()
        print("Pingcam encerrada.")

    def end_game(self):

        self._save_highlights()

        print("\nHighlights registrados:")
        for i, h in enumerate(self.highlight_manager.highlights, start=1):
            print(f"{i:02d}. {h.start:.2f}s → {h.end:.2f}s")

        self.game_running = False

        session_folder = self.session_manager.session_folder

        print("\n=====================================")
        print("Sessão finalizada!")
        print()
        print(f"{len(self.highlight_manager.highlights)} highlights marcados.")
        print()
        print("Próximos passos:")
        print(f"1. Transfira o vídeo do iPhone para a pasta:")
        print(f"   {session_folder}")
        print(f"   nomeando o arquivo como '{native_video_basename}.mp4' (ou .mov)")
        print(f"2. Rode:")
        print(f'   python src/export.py "{session_folder}"')
        print("=====================================")

    def _save_highlights(self):

        data = [asdict(h) for h in self.highlight_manager.highlights]
        path = self.session_manager.session_folder / "highlights.json"

        with open(path, "w") as f:
            json.dump(data, f, indent=2)

        print(f"Highlights salvos em: {path}")