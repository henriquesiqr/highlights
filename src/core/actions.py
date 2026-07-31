from enum import Enum, auto


class Action(Enum):

    NONE = auto()

    START_GAME = auto()

    HIGHLIGHT = auto()

    END_GAME = auto()

    EXIT = auto()