from enum import IntEnum
from random import randint

import pygame as py

from src.helper.game_object import GameObject
from src.helper.game_object_group import GameObjectGroup
from src.minigame1.custom_event import FightDoneEvent


class AI(GameObject):
    def __init__(self, object_group: GameObjectGroup, py_screen, fight_class):
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
        self.blocking = False
        self.hit_range = 20
        self.distance_gap = 0
        self.fight_class = fight_class

    def on_update(self, player_blocking):
        self.blocking = False
        self.distance_gap = self.object_group.distance_to_left(self)
        hit_gap = self.distance_gap - self.hit_range

        behaviour = randint(1, 100)

        if player_blocking:
            if behaviour < 30:
                self.state = AIState.BLOCKING
            else:
                if hit_gap > 20:
                    self.state = AIState.WALKING
                elif hit_gap < 20:
                    self.state = AIState.WALKING_REVERSE
                else:
                    self.state = AIState.IDLE
        elif hit_gap < 20:
            if behaviour < 75:
                self.punching = True
            else:
                self.state = AIState.WALKING_REVERSE
        elif hit_gap > 20:
            self.state = AIState.WALKING
        else:
            self.state = AIState.IDLE

    def is_rendering(self):
        self.drawing = True
        self.render_counter += 1

        # TODO

        return False

    def on_render(self):
        if self.punching:
            self.state = AIState.IDLE
            self.blocking = False
            self.punch()
        else:
            self.punch_rect = None
            draw_map = {1: self.idle,
                        2: self.walk,
                        3: self.walk_r,
                        4: self.block}

            draw_key = self.state.value
            draw_map[draw_key]()
            self.render_counter = 0

    def on_hit(self, player):
        if self.blocking:
            return self.health
        else:
            damage = randint(player.damage_min, player.damage_max)
            if self.health < damage:
                self.health = 0
                py.event.post(FightDoneEvent(self).get_event())
            else:
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
        idle_rect = py.Rect([self.rect.x, self.rect.y], [35, 80])
        py.draw.rect(self.py_screen, [100, 0, 100], idle_rect)
        self.punch_rect = py.Rect([self.rect.left - 35, self.rect.top], [35, 35])
        py.draw.rect(self.py_screen, [100, 0, 100], self.punch_rect)

    def block(self):
        self.blocking = True
        idle_rect = py.Rect([self.rect.x, self.rect.y], [35, 80])
        py.draw.rect(self.py_screen, [254, 254, 254], idle_rect)

    def is_hitting_punch(self, player):
        if self.punching:
            self.punching = False
            return self.punch_rect.colliderect(player.rect)
        return False


class AIState(IntEnum):
    IDLE = 1
    WALKING = 2
    WALKING_REVERSE = 3
    BLOCKING = 4
