import cv2
from pathlib import Path
from core.actions import Action
from core.camera import Camera
from core.game_recorder import GameRecorder
from core.highlight_manager import HighlightManager
from core.video_editor import VideoEditor
from core.session_manager import SessionManager
from core.input_controller import InputController
from core.config import (
    video_codec,
    recordings_dir,
    temp_video_name,
    window_name,
)


class GameSession:

    def __init__(self):

        self.output_path = Path(recordings_dir) / temp_video_name

        self.camera = Camera()

        self.input_controller = InputController()

        self._read_camera_properties()

        self.recorder = None

        self.highlight_manager = HighlightManager()

        self.video_editor = VideoEditor()
        
        self.session_manager = SessionManager()
        
        self.game_running = False

    def _read_camera_properties(self):
 
        self.frame_width = int(
            self.camera.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        )
    
        self.frame_height = int(
            self.camera.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        )
    
        self.camera_fps = self.camera.cap.get(
            cv2.CAP_PROP_FPS
        )
    
        print(
            f"Câmera: "
            f"{self.frame_width}x{self.frame_height} "
            f"@ {self.camera_fps:.2f} FPS"
        )

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

                continue

            # A partir daqui existe uma partida em andamento
            ret, frame = self.camera.read()

            if not ret:
                print("Erro ao capturar frame.")
                break

            cv2.imshow(window_name, frame)

            self.recorder.write(frame)

            if action == Action.HIGHLIGHT:
                self.highlight_manager.add_highlight()

            elif action == Action.END_GAME:
                self.end_game()

            elif action == Action.EXIT:
                self.shutdown()
                break


    def start_game(self):

        self.session_manager = SessionManager()

        self.output_path = (
            self.session_manager.session_folder /
            temp_video_name
        )

        self._read_camera_properties()

        self.recorder = GameRecorder(
            output_path=str(self.output_path),
            width=self.frame_width,
            height=self.frame_height,
            fps=round(self.camera_fps),
            codec=video_codec,
        )

        self.highlight_manager = HighlightManager()

        self.game_running = True

        self.recorder.start()

        print("\nPartida iniciada!")
        
    def export_highlights(self):

        print("\nExportando highlights...")

        success = True

        for highlight in self.highlight_manager.highlights:

            try:
                print(f"Exportando highlight {highlight.id}...")
                
                self.video_editor.export(
                    input_video=str(self.output_path),
                    output_dir=str(self.session_manager.session_folder),
                    highlight=highlight,
                )

            except Exception as e:

                success = False

                print(
                    f"Erro ao exportar highlight "
                    f"{highlight.id}: {e}"
                )

        return success

    def shutdown(self):

        self.input_controller.close()
        self.camera.release()
        cv2.destroyAllWindows()

        print("Pingcam encerrada.")
    
    def end_game(self):

        self.recorder.stop()

        success = self.export_highlights()
        
        if success and self.output_path.exists():
            self.output_path.unlink()
            print("Vídeo temporário removido.")
        elif not success:
            print("Vídeo temporário mantido para recuperação.")

        print("\nHighlights registrados:")

        for i, highlight in enumerate(
            self.highlight_manager.highlights,
            start=1,
        ):

            print(
                f"{i:02d}. "
                f"{highlight.start:.2f}s → "
                f"{highlight.end:.2f}s"
            )
        
        self.game_running = False
            
        print("\n=====================================")
        print("Sessão finalizada!")
        print()
        print(f"{len(self.highlight_manager.highlights)} highlights exportados.")
        print()
        print("Pasta da sessão:")
        print(self.session_manager.session_folder)
        print("=====================================")