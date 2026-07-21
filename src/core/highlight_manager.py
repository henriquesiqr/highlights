import time
from core.highlight import Highlight
from core.config import buffer_seconds


class HighlightManager:

    def __init__(self):

        self.highlights = []

        self.start_time = time.time()

    def add_highlight(self):

        end = time.time() - self.start_time

        start = max(0, end - buffer_seconds)

        highlight = Highlight(
            id=len(self.highlights) + 1,
            start=start,
            end=end,
        )

        self.highlights.append(highlight)

        print(
            f"Highlight registrado "
            f"({highlight.start:.2f}s → {highlight.end:.2f}s)"
        )