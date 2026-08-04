import keyboard

from core.actions import Action
from core.config import (
    key_start,
    key_highlight,
    key_end,
    key_exit,
)


class InputController:

    def __init__(self):

        self.action = Action.NONE

        keyboard.on_press_key(
            key_start,
            lambda _: self._set_action(Action.START_GAME),
        )

        keyboard.on_press_key(
            key_highlight,
            lambda _: self._set_action(Action.HIGHLIGHT),
        )

        keyboard.on_press_key(
            key_end,
            lambda _: self._set_action(Action.END_GAME),
        )

        keyboard.on_press_key(
            key_exit,
            lambda _: self._set_action(Action.EXIT),
        )

    def _set_action(self, action):

        self.action = action

    def get_action(self):

        action = self.action

        self.action = Action.NONE

        return action
    
    def close(self):

        keyboard.unhook_all()