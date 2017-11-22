from enum import IntEnum

import pygame as py

from src.helper.animation import Animation
from src.helper.drawer import Drawer
from src.helper.game_object import GameObject
from src.helper.game_object_group import GameObjectGroup


class Player(GameObject):
    def __init__(self, object_group: GameObjectGroup, py_screen):
        self.player_rect = py.Rect([100, 100], [80, 35])
        self.player_state = PlayerState.IDLE
        self.py_screen = py_screen
        self.velocity = 5
        self.render_counter = 999
        self.solid = True
        self.rect = None
        self.drawer = None
        self.idle_animation = None
        self.walk_animation = None
        super().__init__(object_group, self.velocity, self.solid, self.rect)
        self.load_player_sprite()

    def load_player_sprite(self):
        self.drawer = Drawer.Instance()
        idle_image = self.drawer.load_image("resources/graphics/minigame_1/player_idle.png")
        walk_image = self.drawer.load_image("resources/graphics/minigame_1/player_walk.png")

        self.idle_animation = Animation(self.py_screen, idle_image, 4, 36, 80)
        self.idle_animation.add_scope(0, 0)
        self.idle_animation.add_scope(48, 0)
        self.idle_animation.add_scope(99, 0)
        self.idle_animation.add_scope(148, 0)

        self.walk_animation = Animation(self.py_screen, walk_image, 5, 37, 80)
        self.walk_animation.add_scope(0, 0)
        self.walk_animation.add_scope(42, 0)
        self.walk_animation.add_scope(95, 0)
        self.walk_animation.add_scope(144, 0)
        self.walk_animation.add_scope(189, 0)

    def on_render(self):
        return

    def on_player_render(self, drawer):
        drawing = False
        self.render_counter += 1
        if self.player_state == PlayerState.IDLE:
            if self.render_counter >= 5:
                drawing = True
        elif self.player_state == PlayerState.WALKING:
            if self.render_counter >= 4:
                drawing = True
        elif self.player_state == PlayerState.WALKING_REVERSE:
            if self.render_counter >= 4:
                drawing = True

        draw_map = {1: self.idle,
                    2: self.walk,
                    3: self.walk_r}

        if drawing:
            drawer.draw_canvas()
            draw_key = self.player_state.value
            draw_map[draw_key]()
            self.render_counter = 0

    def idle(self):
        self.idle_animation.on_render(self.player_rect)

    def walk(self):
        self.player_rect.move_ip(4, 0)
        self.walk_animation.on_render(self.player_rect)

    def walk_r(self):
        self.player_rect.move_ip(-4, 0)
        self.walk_animation.on_render(self.player_rect)

    def set_player_state(self, state):
        self.player_state = state


class PlayerState(IntEnum):
    IDLE = 1
    WALKING = 2
    WALKING_REVERSE = 3
