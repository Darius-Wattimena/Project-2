from src.helper.screen_base import ScreenBase
from src.helper.game_object_group import GameObjectGroup
from src.minigame1.ai import AI
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
        self.ai = AI(self.game_object_group, self.game.py_screen)
        self.first = True

    def on_events(self, events):
        return

    def on_render(self):
        if self.player.is_rendering() or self.ai.is_rendering():
            self.game.drawer.draw_canvas()
            self.player.on_render()
            self.ai.on_render()
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
        elif keys[py.K_j]:
            self.player.set_player_state(PlayerState.PUNCHING)
        else:
            self.player.set_player_state(PlayerState.IDLE)

        return
