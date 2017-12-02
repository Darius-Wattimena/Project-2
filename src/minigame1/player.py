from enum import IntEnum

import pygame as py

from src.helper.animation import Animation
from src.helper.drawer import Drawer
from src.helper.game_object import GameObject
from src.helper.game_object_group import GameObjectGroup


class Player(GameObject):
    def __init__(self, object_group: GameObjectGroup, py_screen):
        super().__init__(object_group, 1, True, py.Rect([100, 100], [35, 80]))
        self.health = 100
        self.state = PlayerState.IDLE
        self.py_screen = py_screen
        self.render_counter = 999
        self.drawing = False
        self.drawer = None
        self.idle_animation = None
        self.walk_animation = None
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

    def is_rendering(self):
        self.drawing = False
        self.render_counter += 1
        if self.state == PlayerState.IDLE:
            if self.render_counter >= 5:
                self.drawing = True
        elif self.state == PlayerState.WALKING:
            if self.render_counter >= 4:
                self.drawing = True
        elif self.state == PlayerState.WALKING_REVERSE:
            if self.render_counter >= 4:
                self.drawing = True
        elif self.state == PlayerState.PUNCHING:
            self.drawing = True
        return self.drawing

    def on_render(self):
        draw_map = {1: self.idle,
                    2: self.walk,
                    3: self.walk_r,
                    4: self.punch}

        draw_key = self.state.value
        draw_map[draw_key]()
        self.render_counter = 0

    def on_hit(self, damage):
        self.health -= damage

    def idle(self):
        if self.drawing:
            self.idle_animation.on_render(self.rect)
        else:
            self.idle_animation.on_old_render(self.rect)

    def walk(self):
        distance_gap = self.object_group.distance_to_right(self)
        if distance_gap >= 4:
            self.rect.move_ip(4, 0)
        elif distance_gap >= 1:
            self.rect.move_ip(distance_gap, 0)

        if self.drawing:
            self.walk_animation.on_render(self.rect)
        else:
            self.walk_animation.on_old_render(self.rect)

    def walk_r(self):
        self.rect.move_ip(-4, 0)
        if self.drawing:
            self.walk_animation.on_render(self.rect)
        else:
            self.walk_animation.on_old_render(self.rect)

    def punch(self):
        punch_rect = py.Rect([self.rect.right, self.rect.top], [35, 35])
        py.draw.rect(self.py_screen, [100, 0, 100], punch_rect)

    def set_player_state(self, state):
        self.state = state


class PlayerState(IntEnum):
    IDLE = 1
    WALKING = 2
    WALKING_REVERSE = 3
    PUNCHING = 4
