from pathlib import Path
from datetime import datetime


class SessionManager:

    def __init__(self):

        self.session_folder = self._create_session_folder()

    def _create_session_folder(self):

        date = datetime.now().strftime("%Y%m%d")

        highlights_root = Path("highlights")

        session = 1

        while True:

            folder = highlights_root / f"{date}_s{session:02d}"

            if not folder.exists():
                folder.mkdir(parents=True)
                return folder

            session += 1