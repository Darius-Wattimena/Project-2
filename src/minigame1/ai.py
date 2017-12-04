from enum import IntEnum
from random import randint

import pygame as py

from src.helper.game_object import GameObject
from src.helper.game_object_group import GameObjectGroup


class AI(GameObject):
    def __init__(self, object_group: GameObjectGroup, py_screen):
        super().__init__(object_group, 1, True, py.Rect([200, 100], [35, 80]))
        self.damage_max = 10
        self.damage_min = 3
        self.health = 100
        self.state = AIState.IDLE
        self.py_screen = py_screen
        self.render_counter = 999
        self.drawing = False
        self.idle_animation = None
        self.walk_animation = None
        self.punching = False
        self.punch_rect = None
        self.punch_animation = None
        self.punch_animation_running = False
        self.hit_range = 20
        self.distance_gap = 0

    def on_update(self):
        self.distance_gap = self.object_group.distance_to_left(self)
        hit_gap = self.distance_gap - self.hit_range
        if hit_gap > 20:
            self.state = AIState.WALKING
        elif hit_gap < 20:
            self.state = AIState.WALKING_REVERSE
        else:
            self.state = AIState.IDLE

    def is_rendering(self):
        self.drawing = True
        self.render_counter += 1

        # TODO

        return False

    def on_render(self):
        draw_map = {1: self.idle,
                    2: self.walk,
                    3: self.walk_r}

        draw_key = self.state.value
        draw_map[draw_key]()
        self.render_counter = 0

    def on_hit(self, player):
        damage = randint(player.damage_min, player.damage_max)
        self.health -= damage
        return self.health

    def idle(self):
        """
        if self.drawing:
            self.idle_animation.on_render(self.rect)
        else:
            self.idle_animation.on_old_render(self.rect)
        """
        idle_rect = py.Rect([self.rect.x, self.rect.y], [35, 80])
        py.draw.rect(self.py_screen, [100, 0, 100], idle_rect)

    def walk(self):
        distance = self.distance_gap - self.hit_range
        if distance >= 4 + self.hit_range:
            self.rect.move_ip(-4, 0)
        elif distance >= 1 + self.hit_range:
            self.rect.move_ip(-(distance - self.hit_range), 0)

        idle_rect = py.Rect([self.rect.x, self.rect.y], [35, 80])
        py.draw.rect(self.py_screen, [100, 0, 100], idle_rect)

        self.state = AIState.IDLE
        """
        if self.drawing:
            self.walk_animation.on_render(self.rect)
        else:
            self.walk_animation.on_old_render(self.rect)
        """

    def walk_r(self):
        distance = self.distance_gap - self.hit_range
        if distance >= 4 - self.hit_range:
            self.rect.move_ip(4, 0)
        elif distance >= 1 - self.hit_range:
            self.rect.move_ip(distance - self.hit_range, 0)

        idle_rect = py.Rect([self.rect.x, self.rect.y], [35, 80])
        py.draw.rect(self.py_screen, [100, 0, 100], idle_rect)

        self.state = AIState.IDLE
        """
        self.rect.move_ip(4, 0)
        if self.drawing:
            self.walk_animation.on_render(self.rect)
        else:
            self.walk_animation.on_old_render(self.rect)
        """

    def punch(self):
        punch_rect = py.Rect([self.rect.right, self.rect.top], [35, 35])
        py.draw.rect(self.py_screen, [100, 0, 100], punch_rect)

    def is_hitting_punch(self, player):
        if self.punching:
            self.punching = False
            return self.punch_rect.colliderect(player.rect)
        return False


class AIState(IntEnum):
    IDLE = 1
    WALKING = 2
    WALKING_REVERSE = 3
