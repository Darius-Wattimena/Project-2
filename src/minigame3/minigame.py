import pygame as py

from src.helper.label import Label
from ..helper.screen_base import ScreenBase
from .enemy import enemy
from src.helper.drawer import Drawer


class Minigame_3(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.enemy_is_spawned = True
        self.enemy_is_moving = True
        self.groundcolor = (240, 230, 140)
        self.skycolor = (20, 20, 255)

        self.groundrect = py.Rect([0, 250], [1280, 720])
        self.skyrect = py.Rect([0, 0], [1280, 250])

        self.player()
        self.enemy()

        self.spawn_event = py.USEREVENT + 1
        self.time_between_spawn = 3000
        py.time.set_timer(self.spawn_event, self.time_between_spawn)

        self.move_event = py.USEREVENT + 2
        self.time_between_movement = 5
        py.time.set_timer(self.move_event, self.time_between_spawn)

        self.collide_event = py.USEREVENT + 3

        self.lives_label = Label(self.game.py_screen, "Current Lives: " + str(self.lives), [0, 0, 0], 50)

    def player(self):
        player_width = 100
        player_height = 100
        self.player_image = py.image.load("resources/graphics/minigame_3/testimage.png")
        # Resize je foto omdat de photo kleiner is dan de player rect
        self.player_image = py.transform.scale(self.player_image, [player_width, player_height])
        self.player_rect = py.Rect([640, 650], [player_width, player_height])
        self.lives = 100

    def enemy(self):
        enemy_width = 100
        enemy_height = 100
        self.enemy_image = py.image.load("resources/graphics/minigame_3/testimage.png")
        # Resize je foto omdat de photo kleiner is dan de enemy rect
        self.enemy_image = py.transform.scale(self.enemy_image, [enemy_width, enemy_height])
        self.enemy_location = enemy.get_location(self)
        self.enemy_rect = py.Rect(self.enemy_location, [enemy_width, enemy_height])

    def on_events(self, events):
        for event in events:
            if event.type == self.spawn_event:
                self.enemy_is_spawned = True
                self.selected_location = enemy.get_location(self)
                self.enemy_rect.x = self.selected_location[0]
                self.enemy_rect.y = self.selected_location[1]
            if event.type == self.move_event:
                self.enemy_is_moving = True
                self.enemy_rect.move_ip(0, 2)
                py.time.set_timer(self.move_event, self.time_between_movement)
            if event.type == self.collide_event:
                collision = self.player_rect.colliderect(self.enemy_rect)
                if collision:
                    # TODO despawn enemy when collided
                    if self.lives > 0:
                        self.lives -= 1
                        self.lives_label.text = "Current Lives: " + str(self.lives)
                    elif self.lives == 0:
                        self.lives_label.text = "You Died!!"

    def on_update(self):
        # Elke frame roepen wij deze event aan en kijken we of er collision is
        py.event.post(py.event.Event(self.collide_event))

    def on_render(self):
        self.game.drawer.draw_canvas()
        py.draw.rect(self.game.py_screen, self.groundcolor, self.groundrect)
        py.draw.rect(self.game.py_screen, self.skycolor, self.skyrect)
        self.game.py_screen.blit(self.player_image, self.player_rect)

        if self.enemy_is_spawned is True:
            py.draw.rect(self.game.py_screen, [0, 0, 0], self.enemy_rect)
            self.game.py_screen.blit(self.enemy_image, self.enemy_rect)
        if self.enemy_is_moving is True:
            py.draw.rect(self.game.py_screen, [0, 0, 0], self.enemy_rect)
            self.game.py_screen.blit(self.enemy_image, self.enemy_rect)
        self.lives_label.render(100, 100)
        py.display.update()

    def handle_mouse_input(self, mouse):
        return

    def handle_key_input(self, keys):
        if keys[py.K_a]:
            self.player_rect.move_ip(-10, 0)
        elif keys[py.K_d]:
            self.player_rect.move_ip(10, 0)
        elif keys[py.K_w]:
            self.enemy_rect.move_ip(0, 5)
        elif keys[py.K_s]:
            self.enemy_rect.move_ip(0, -1)
        return

    def handle_mouse_position(self, mouse_position):
        return
