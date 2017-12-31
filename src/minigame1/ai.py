from enum import IntEnum
from random import randint

import pygame as py

from src.helper.animation import Animation
from src.helper.game_object import GameObject
from src.helper.game_object_group import GameObjectGroup
from src.minigame1.custom_event import FightDoneEvent


class AI(GameObject):
    def __init__(self, object_group: GameObjectGroup, py_screen, debug):
        super().__init__(object_group, 1, True, py.Rect([800, 400], [35 * 3, 80 * 3]))
        self.debug = debug
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
        self.punch_render_counter = 0
        self.hit_animation = None
        self.hit_animation_running = False
        self.hit_render_counter = 0
        self.blocking = False
        self.hit_range = 27 * 3
        self.distance_gap = 0
        self.load_ai_sprite()
        self.block_image = self.load_sprite("resources/graphics/minigame_1/ai/block2.png")
        self.block_image_rect_base = self.block_image.get_rect()

    def load_ai_sprite(self):
        idle_image = self.load_sprite("resources/graphics/minigame_1/ai/idle2.png")
        walk_image = self.load_sprite("resources/graphics/minigame_1/ai/walk2.png")
        punch_image = self.load_sprite("resources/graphics/minigame_1/ai/punch2.png")
        hit_image = self.load_sprite("resources/graphics/minigame_1/hit_effect.png")

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

        self.hit_animation = Animation(self.py_screen, hit_image, 4, 192, 192)
        self.hit_animation.add_scope(0, 0)
        self.hit_animation.add_scope(192, 0)
        self.hit_animation.add_scope(384, 0)
        self.hit_animation.add_scope(576, 0)

    def load_sprite(self, resource_location):
        image = py.image.load(resource_location).convert_alpha()
        return self.mirror_sprite(image)

    def mirror_sprite(self, surface):
        return py.transform.flip(surface, True, False)

    def is_rendering(self):
        self.drawing = False
        self.render_counter += 1
        if self.state == AIState.BLOCKING or self.punching:
            self.drawing = True
        elif self.state == AIState.IDLE:
            if self.render_counter >= 4:
                self.drawing = True
                self.render_counter = 0
        elif self.state == AIState.WALKING:
            if self.render_counter >= 4:
                self.drawing = True
                self.render_counter = 0
        elif self.state == AIState.WALKING_REVERSE:
            if self.render_counter >= 4:
                self.drawing = True
                self.render_counter = 0
        return self.drawing

    def on_render(self):
        # hitbox
        if self.debug:
            py.draw.rect(self.py_screen, [0, 255, 0], self.rect, 2)

        # render
        if self.punch_animation_running:
            # hitbox
            if self.debug:
                py.draw.rect(self.py_screen, [0, 255, 0], self.punch_rect, 2)

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
                self.punch_render_counter += 1
                if self.punch_render_counter >= 2:
                    # Render punch animation
                    self.punch_animation.on_render(self.rect)
                    self.punch_render_counter = 0
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
        if self.hit_animation_running:
            if self.hit_animation.current_animation == self.hit_animation.animation_count:
                self.hit_animation.current_animation = 0
                self.hit_animation_running = False
            else:
                self.hit_render_counter += 1
                if self.hit_render_counter >= 2:
                    self.hit_animation.on_render(self.hit_rect)
                    self.hit_render_counter = 0
                else:
                    self.hit_animation.on_old_render(self.hit_rect)

    def on_hit(self, player):
        if self.blocking:
            return self.health
        else:
            self.hit_animation_running = True
            self.hit_rect = py.Rect(self.rect)
            self.hit_rect.x -= 50
            self.hit_rect.y -= 20

            damage = randint(player.damage_min, player.damage_max)
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
        if self.drawing:
            distance = self.distance_gap - self.hit_range
            if distance >= (12 + self.hit_range):
                self.rect.move_ip(-12, 0)
            elif distance >= (1 + self.hit_range):
                self.rect.move_ip(-(distance - self.hit_range), 0)
            self.walk_animation.on_render(self.rect)
        else:
            self.walk_animation.on_old_render(self.rect)

    def walk_r(self):
        if self.drawing:
            self.rect.move_ip(12, 0)
            self.walk_animation.on_render(self.rect)
        else:
            self.walk_animation.on_old_render(self.rect)

    def punch(self):
        self.punch_rect = py.Rect([self.rect.left - (27 * 3), self.rect.top], [27 * 3, 35 * 3])
        self.punch_animation_running = True
        self.idle_animation.on_old_render(self.rect)

    def block(self):
        self.blocking = True

        block_image_rect = self.block_image_rect_base
        block_image_rect.x = self.rect.x
        block_image_rect.y = self.rect.y
        self.py_screen.blit(self.block_image, block_image_rect)

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
