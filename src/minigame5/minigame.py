import pygame as py
import time
from ..helper.screen_base import ScreenBase
from .Target import Target
from random import *

class Minigame_5(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.game.drawer.clear()

        # Defines BACKGROUND and BUILDINGS
        self.background_img = py.image.load("resources/graphics/minigame_5/background.png")
        self.building_exterior_img = py.image.load("resources/graphics/minigame_5/building_exterior.png")
        self.building_interior_img = py.image.load("resources/graphics/minigame_5/building_interior.png")

        # Defines GUN
        self.gun_leftfar = py.image.load("resources/graphics/minigame_5/gunposleftfar.png")
        self.gun_leftclose = py.image.load("resources/graphics/minigame_5/gunposleftclose.png")
        self.gun_central = py.image.load("resources/graphics/minigame_5/gunposcentral.png")
        self.gun_rightclose = py.image.load("resources/graphics/minigame_5/gunposrightclose.png")
        self.gun_rightfar = py.image.load("resources/graphics/minigame_5/gunposrightfar.png")
        self.gun_shot = py.image.load("resources/graphics/minigame_5/bulletshot.png")
        self.gun_impact = py.image.load("resources/graphics/minigame_5/bulletimpact.png")
        self.gun_rect = py.Rect(468, 560, 50, 50)
        py.draw.rect(self.game.py_screen, [0, 0, 0], self.gun_rect)

        # Defines TARGET, based on Target.py
        self.target_img = py.image.load("resources/graphics/minigame_5/target.png")
        self.spawn_location = Target.random_location(self)
        self.target_rect = py.Rect(self.spawn_location, [45, 90])
        py.draw.rect(self.game.py_screen, [0, 0, 0], self.target_rect)

        # Defines CROSSHAIR
        self.crosshair_img = py.image.load("resources/graphics/minigame_5/crosshair_white_red_40p.png")
        self.crosshair_collide_img = py.image.load("resources/graphics/minigame_5/crosshair_white_green_40p.png")
        self.crosshair_x = 640
        self.crosshair_y = 360
        self.crosshair_speed = 30
        self.crosshair_rect = py.Rect([self.crosshair_x, self.crosshair_y], [40, 40])

        # Defines EVENTS, TEXT and TIMER
        self.spawn_event = py.USEREVENT + 1
        self.spawn_time = 3000
        self.showing_target = True
        py.time.set_timer(self.spawn_event, self.spawn_time)

        self.reload_event = py.USEREVENT + 2
        self.reload_speed = 400
        self.reloaded_gun = True

        self.gun_shot_disappear_event = py.USEREVENT + 3
        self.time_till_shot_disappear = 60
        self.gun_shot_succes = False
        self.gun_direction = 0

        self.gun_status_event = py.USEREVENT + 4
        self.time_till_gun_status_text_disappears = 1000
        self.gun_status_display = False
        self.gun_status_font = py.font.Font("resources/fonts/Carnevalee Freakshow.ttf", 60)
        self.gun_status = 0
        self.gun_text_string = ""
        self.gun_text_color = (255, 255, 255)
        self.gun_status_text = self.gun_status_font.render(self.gun_text_string, 1, (255, 255, 255))

        self.score_font = py.font.Font("resources/fonts/Carnevalee Freakshow.ttf", 40)
        self.score = 0

        self.timer_font = py.font.Font("resources/fonts/Carnevalee Freakshow.ttf", 40)
        self.game_duration = 120
        self.starting_timer = time.time()

    def on_events(self, events):
        for event in events:
            if event.type == self.reload_event:
                self.reloaded_gun = True
                py.time.set_timer(self.reload_event, 0)
            elif event.type == self.spawn_event:
                self.showing_target = True
                self.selected_location = Target.random_location(self)
                self.target_rect.x = self.selected_location[0]
                self.target_rect.y = self.selected_location[1]
                py.time.set_timer(self.spawn_event, self.spawn_time)
            elif event.type == self.gun_shot_disappear_event:
                self.gun_shot_succes = False
                py.time.set_timer(self.gun_shot_disappear_event, 0)
            elif event.type == self.gun_status_event:
                self.gun_status_display = False
                py.time.set_timer(self.gun_status_event, 0)
            elif event.type == py.QUIT:
                break
        return

    def on_update(self):
        py.time.get_ticks()
        return

    def on_render(self):
        self.game.drawer.draw_canvas()

        # Time Tracker
        self.check_time = time.time()
        self.time_left = self.game_duration - int(self.check_time - self.starting_timer)

        # Displays BACKGROUND and BUILDINGS interior
        self.game.py_screen.blit(self.background_img, [0, 0])
        self.game.py_screen.blit(self.building_interior_img, [0, 0])

        # Displays TARGET
        if self.showing_target:
            py.draw.rect(self.game.py_screen, [0, 0, 0], self.target_rect)
            self.game.py_screen.blit(self.target_img, self.target_rect)

        # Displays BUILDINGS exterior
        self.game.py_screen.blit(self.building_exterior_img, [0, 0])

        # Displays GUN shots at GUN
        if self.gun_shot_succes:
            if self.gun_direction == 0:
                self.game.py_screen.blit(self.gun_shot, [625, 550])
                self.game.py_screen.blit(self.gun_impact, self.crosshair_rect)
            elif self.gun_direction == 1:
                self.game.py_screen.blit(self.gun_shot, [758, 580])
                self.game.py_screen.blit(self.gun_impact, self.crosshair_rect)
            elif self.gun_direction == 2:
                self.game.py_screen.blit(self.gun_shot, [795, 628])
                self.game.py_screen.blit(self.gun_impact, self.crosshair_rect)
            elif self.gun_direction == 3:
                self.game.py_screen.blit(self.gun_shot, [488, 578])
                self.game.py_screen.blit(self.gun_impact, self.crosshair_rect)
            elif self.gun_direction == 4:
                self.game.py_screen.blit(self.gun_shot, [455, 624])
                self.game.py_screen.blit(self.gun_impact, self.crosshair_rect)
        elif not self.gun_shot_succes:
            pass

        #Displays GUN, img based on x pos of crosshair_rect
        if self.crosshair_rect[0] >= 490:
            if self.crosshair_rect[0] <= 790:
                self.gun_direction = 0
                self.game.py_screen.blit(self.gun_central, self.gun_rect)
            elif self.crosshair_rect[0] >= 791:
                if self.crosshair_rect[0] <= 900:
                    self.gun_direction = 1
                    self.game.py_screen.blit(self.gun_rightclose, self.gun_rect)
                elif self.crosshair_rect[0] >= 901:
                    if self.crosshair_rect[0] <= 1280:
                        self.gun_direction = 2
                        self.game.py_screen.blit(self.gun_rightfar, self.gun_rect)
        elif self.crosshair_rect[0] >= 200:
            if self.crosshair_rect[0] <= 489:
                self.gun_direction = 3
                self.game.py_screen.blit(self.gun_leftclose, self.gun_rect)
        elif self.crosshair_rect[0] >= 0:
            if self.crosshair_rect[0] <= 199:
                self.gun_direction = 4
                self.game.py_screen.blit(self.gun_leftfar, self.gun_rect)

        # Displays SCORE, TIME, TARGET COUNTER
        self.display_score = self.score_font.render("Score: " + str(self.score), 1, (249, 239, 176))
        self.game.py_screen.blit(self.display_score, (940, 10))

        self.display_game_time = self.timer_font.render("Time left: " + str(self.time_left) + " secs", 1, (249, 239, 176))
        self.game.py_screen.blit(self.display_game_time, (240, 10))

        # Displays GUN STATUS
        if self.gun_status_display:
            self.gun_status_text = self.gun_status_font.render(self.gun_text_string, 1, self.gun_text_color)
            self.game.py_screen.blit(self.gun_status_text, (100, 650))
            if self.gun_status == 1:
                self.gun_text_string = "Good shot!"
                self.gun_text_color = (139, 234, 87)
            if self.gun_status == 2:
                self.gun_text_string = "Miss!"
                self.gun_text_color = (215, 65, 65)

        # Displays CROSSHAIR, clamps it to screen, sets it's collision
        self.crosshair_rect.clamp_ip(self.game.py_screen.get_rect())
        self.collidecheck = self.crosshair_rect.colliderect(self.target_rect)

        if self.collidecheck:
            self.game.py_screen.blit(self.crosshair_collide_img, self.crosshair_rect)
        elif not self.collidecheck:
            self.game.py_screen.blit(self.crosshair_img, self.crosshair_rect)

        py.display.update()
        return

    def handle_mouse_input(self, mouse):
        return

    def handle_key_input(self, keys):
        if keys[py.K_w]:
            self.crosshair_rect.move_ip(0, -self.crosshair_speed)
        elif keys[py.K_a]:
            self.crosshair_rect.move_ip(-self.crosshair_speed, 0)
        elif keys[py.K_s]:
            self.crosshair_rect.move_ip(0, +self.crosshair_speed)
        elif keys[py.K_d]:
            self.crosshair_rect.move_ip(+self.crosshair_speed, 0)

        elif keys[py.K_SPACE]:
            if self.reloaded_gun:
                if self.collidecheck:
                    self.reloaded_gun = False
                    self.showing_target = False
                    self.gun_status = 1
                    self.gun_shot_succes = True
                    self.gun_status_display = True
                    self.target_rect.x = 1280
                    py.time.set_timer(self.reload_event, self.reload_speed)
                    py.time.set_timer(self.gun_shot_disappear_event, self.time_till_shot_disappear)
                    py.time.set_timer(self.gun_status_event, self.time_till_gun_status_text_disappears)
                    self.score += 10

                if not self.collidecheck:
                    self.reloaded_gun = False
                    self.gun_status = 2
                    self.gun_shot_succes = True
                    self.gun_status_display = True
                    py.time.set_timer(self.reload_event, self.reload_speed)
                    py.time.set_timer(self.gun_shot_disappear_event, self.time_till_shot_disappear)
                    py.time.set_timer(self.gun_status_event, self.time_till_gun_status_text_disappears)
                    self.score -= 5
            if not self.reloaded_gun:
                pass

        elif keys[py.K_1]:
            self.spawn_time = 1000
        elif keys[py.K_2]:
            self.spawn_time = 2000
        elif keys[py.K_3]:
            self.spawn_time = 3000 # default
        elif keys[py.K_4]:
            self.spawn_time = 4000
        elif keys[py.K_5]:
            self.spawn_time = 5000
        elif keys[py.K_6]:
            self.crosshair_speed = 30 # default
        elif keys[py.K_7]:
            self.crosshair_speed = 35
        elif keys[py.K_8]:
            self.crosshair_speed = 40
        elif keys[py.K_9]:
            self.crosshair_speed = 45
        elif keys[py.K_0]:
            self.crosshair_speed = 50
        return

    def handle_mouse_position(self, mouse_position):
        return