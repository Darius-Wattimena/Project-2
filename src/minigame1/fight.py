from src.helper.screen_base import ScreenBase
from src.helper.game_object_group import GameObjectGroup
from .player import Player, PlayerState
import pygame as py


class Fight(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.game_object_group = GameObjectGroup()
        self.game.drawer.clear()
        self.game.drawer.add_image("resources/graphics/minigame_1/background.png")
        self.player = Player(self.game_object_group, self.game.py_screen)
        self.first = True

    def on_events(self, events):
        return

    def on_render(self):
        self.player.on_player_render(self.game.drawer)
        py.display.update()

    def on_update(self):
        return

    def handle_mouse_position(self, mouse_position):
        return

    def handle_mouse_input(self, event):
        return

    def handle_key_input(self, keys):
        if keys[py.K_d]:
            self.player.set_player_state(PlayerState.WALKING)
        elif keys[py.K_a]:
            self.player.set_player_state(PlayerState.WALKING_REVERSE)
        else:
            self.player.set_player_state(PlayerState.IDLE)

        return
