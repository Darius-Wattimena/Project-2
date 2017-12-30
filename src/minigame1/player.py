from enum import IntEnum
from random import randint

import pygame as py

from src.helper.animation import Animation
from src.helper.drawer import Drawer
from src.helper.game_object import GameObject
from src.helper.game_object_group import GameObjectGroup
from src.minigame1.custom_event import FightDoneEvent


class Player(GameObject):
    def __init__(self, object_group: GameObjectGroup, py_screen, fight_class):
        super().__init__(object_group, 1, True, py.Rect([100, 400], [35 * 3, 80 * 3]))
        self.damage_max = 10
        self.damage_min = 3
        self.health = 100
        self.state = PlayerState.IDLE
        self.py_screen = py_screen
        self.render_counter = 999
        self.drawing = False
        self.drawer = None
        self.idle_animation = None
        self.walk_animation = None
        self.punching = False
        self.punch_rect = None
        self.punch_animation = None
        self.punch_animation_running = False
        self.blocking = False
        self.won_fight = None
        self.fight_class = fight_class
        self.load_player_sprite()
        self.block_image = py.image.load("resources/graphics/minigame_1/player/block2.png").convert_alpha()
        self.block_image_rect_base = self.block_image.get_rect()

    def load_player_sprite(self):
        self.drawer = Drawer.Instance()
        idle_image = py.image.load("resources/graphics/minigame_1/player/idle2.png").convert_alpha()
        walk_image = py.image.load("resources/graphics/minigame_1/player/walk2.png").convert_alpha()
        punch_image = py.image.load("resources/graphics/minigame_1/player/punch2.png").convert_alpha()

        self.idle_animation = Animation(self.py_screen, idle_image, 4, 36 * 3, 80 * 3)
        self.idle_animation.add_scope(0, 0)
        self.idle_animation.add_scope(48 * 3, 0)
        self.idle_animation.add_scope(99 * 3, 0)
        self.idle_animation.add_scope(148 * 3, 0)

        self.walk_animation = Animation(self.py_screen, walk_image, 5, 37 * 3, 80 * 3)
        self.walk_animation.add_scope(0, 0)
        self.walk_animation.add_scope(42 * 3, 0)
        self.walk_animation.add_scope(95 * 3, 0)
        self.walk_animation.add_scope(144 * 3, 0)
        self.walk_animation.add_scope(189 * 3, 0)

        self.punch_animation = Animation(self.py_screen, punch_image, 5, 38 * 3, 80 * 3)
        self.punch_animation.add_scope(0, 0)
        self.punch_animation.add_scope(51 * 3, 0)
        self.punch_animation.add_scope(110 * 3, 0)
        self.punch_animation.add_scope(186 * 3, 0)
        self.punch_animation.add_scope(241 * 3, 0)

    def is_rendering(self):
        self.drawing = False
        self.render_counter += 1
        if self.state == PlayerState.BLOCKING or self.punching:
            self.drawing = True
        elif self.state == PlayerState.IDLE:
            if self.render_counter >= 5:
                self.drawing = True
        elif self.state == PlayerState.WALKING:
            if self.render_counter >= 4:
                self.drawing = True
        elif self.state == PlayerState.WALKING_REVERSE:
            if self.render_counter >= 4:
                self.drawing = True
        return self.drawing

    def on_render(self):
        if self.punch_animation_running:
            if self.punch_animation.current_animation == 3:
                self.punch_animation.rect.width = 68 * 3
            elif self.punch_animation.current_animation == 4:
                self.punch_animation.rect.width = 38 * 3

            # Stop punch animation if finished
            if self.punch_animation.current_animation == self.punch_animation.animation_count:
                self.punch_animation.current_animation = 1
                self.punch_animation_running = False
            else:
                # Check if we need a new animation
                self.drawing = False
                self.render_counter += 1
                if self.render_counter >= 5:
                    # Render punch animation
                    self.drawing = True
                    self.punch_animation.on_render(self.rect)
                    self.render_counter = 0
                else:
                    # Render old punch animation when we do not need a new frame
                    self.punch_animation.on_old_render(self.rect)
        elif self.punching:
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

    def on_hit(self, ai):
        if self.blocking:
            return self.health
        else:
            damage = randint(ai.damage_min, ai.damage_max)
            if self.health < damage:
                self.health = 0
                py.event.post(FightDoneEvent(self).get_event())
            else:
                self.health -= damage
            return self.health

    def idle(self):
        if self.drawing:
            self.idle_animation.on_render(self.rect)
        else:
            self.idle_animation.on_old_render(self.rect)

    def walk(self):
        distance_gap = self.object_group.distance_to_right(self)
        if distance_gap >= (4 * 3):
            self.rect.move_ip(4 * 3, 0)
        elif distance_gap >= 1:
            self.rect.move_ip(distance_gap, 0)

        if self.drawing:
            self.walk_animation.on_render(self.rect)
        else:
            self.walk_animation.on_old_render(self.rect)

    def walk_r(self):
        self.rect.move_ip(-4 * 3, 0)
        if self.drawing:
            self.walk_animation.on_render(self.rect)
        else:
            self.walk_animation.on_old_render(self.rect)

    def punch(self):
        self.punch_rect = py.Rect([self.rect.right, self.rect.top], [27 * 3, 35 * 3])
        self.punch_animation_running = True

    def block(self):
        self.blocking = True

        block_image_rect = self.block_image_rect_base
        block_image_rect.x = self.rect.x
        block_image_rect.y = self.rect.y
        self.py_screen.blit(self.block_image, block_image_rect)

    def set_state(self, state):
        self.state = state

    def is_hitting_punch(self, ai):
        if self.punching:
            self.punching = False
            return self.punch_rect.colliderect(ai.rect)
        return False


class PlayerState(IntEnum):
    IDLE = 1
    WALKING = 2
    WALKING_REVERSE = 3
    BLOCKING = 4
