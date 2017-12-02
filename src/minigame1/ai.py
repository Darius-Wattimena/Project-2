from enum import IntEnum

import pygame as py

from src.helper.game_object import GameObject
from src.helper.game_object_group import GameObjectGroup


class AI(GameObject):
    def __init__(self, object_group: GameObjectGroup, py_screen):
        super().__init__(object_group, 1, True, py.Rect([200, 100], [35, 80]))
        self.health = 100
        self.state = AIState.IDLE
        self.py_screen = py_screen
        self.render_counter = 999

    def is_rendering(self):
        drawing = True
        self.render_counter += 1

        # TODO

        return False

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
        idle_rect = py.Rect([self.rect.x, self.rect.y], [35, 80])
        py.draw.rect(self.py_screen, [100, 0, 100], idle_rect)

    def walk(self):
        self.rect.move_ip(-4, 0)
        return

    def walk_r(self):
        self.rect.move_ip(4, 0)
        return

    def punch(self):
        punch_rect = py.Rect([self.rect.right, self.rect.top], [35, 35])
        py.draw.rect(self.py_screen, [100, 0, 100], punch_rect)


class AIState(IntEnum):
    IDLE = 1
    WALKING = 2
    WALKING_REVERSE = 3
    PUNCHING = 4
