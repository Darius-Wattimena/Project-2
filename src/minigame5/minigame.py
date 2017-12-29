import time

import pygame as py

from .target import Target
from ..helper.screen_base import ScreenBase
from ..helper.label import Label
from ..helper.image_button import ImageButton


class Minigame_5(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.game.drawer.clear()
        self.screen_center_width = self.game.py_screen.get_width() / 2
        self.mouse_position = None

        # Defines BACKGROUND and BUILDINGS
        self.background_img = py.image.load("resources/graphics/minigame_5/background.png")
        self.dark_surface = py.Surface((1280, 720))
        self.dark_surface.set_alpha(170)
        self.building_exterior_img = py.image.load("resources/graphics/minigame_5/building_exterior.png")
        self.building_interior_img = py.image.load("resources/graphics/minigame_5/building_interior.png")
        self.building_shadows_img = py.image.load("resources/graphics/minigame_5/building_shadows.png")

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

        # Defines TARGET, based on target.py
        self.target_img = py.image.load("resources/graphics/minigame_5/target.png")
        self.target = Target()
        self.selected_location = self.target.get_location()
        self.selected_location2 = self.target.get_location()
        self.target_rect = py.Rect((self.selected_location[0], self.selected_location[1]),
                                   (self.selected_location[2], self.selected_location[3]))
        self.target_rect2 = py.Rect((self.selected_location2[0], self.selected_location2[1]),
                                    (self.selected_location2[2], self.selected_location2[3]))
        py.draw.rect(self.game.py_screen, [0, 0, 0], self.target_rect)
        py.draw.rect(self.game.py_screen, [0, 0, 0], self.target_rect2)

        # Defines CROSSHAIR
        self.crosshair_img = py.image.load("resources/graphics/minigame_5/crosshair_white_red_40p.png")
        self.crosshair_collide_img = py.image.load("resources/graphics/minigame_5/crosshair_white_green_40p.png")
        self.crosshair_x = 640
        self.crosshair_y = 360
        self.crosshair_speed = 35
        self.crosshair_rect = py.Rect([self.crosshair_x, self.crosshair_y], [40, 40])

        # Defines EVENTS, TEXT
        self.spawn_event = py.USEREVENT + 1
        self.spawn_time = 3000
        self.showing_target = True
        self.showing_target2 = True
        py.time.set_timer(self.spawn_event, self.spawn_time)

        self.reload_event = py.USEREVENT + 2
        self.reload_speed = 400
        self.reloaded_gun = True

        self.gun_shot_disappear_event = py.USEREVENT + 3
        self.time_till_shot_disappear = 60
        self.gun_shot_succes = False
        self.gun_direction = 0
        py.mixer.music.load("resources/graphics/minigame_5/gun-gunshot-02.mp3")

        self.gun_status_event = py.USEREVENT + 4
        self.time_till_gun_status_text_disappears = 1000
        self.gun_status_display = False
        self.gun_status_font = py.font.Font("resources/fonts/Carnevalee Freakshow.ttf", 60)
        self.gun_status = 0
        self.gun_text_string = ""
        self.gun_text_color = (255, 255, 255)
        self.gun_status_text = self.gun_status_font.render(self.gun_text_string, 1, (255, 255, 255))

        self.score_font = py.font.Font("resources/fonts/Carnevalee Freakshow.ttf", 40)
        self.score_count_font = py.font.Font("resources/fonts/Carnevalee Freakshow.ttf", 70)
        self.score = 0
        self.target_counter = 0
        self.miss_counter = 0

        # Defines TIMER
        self.time_font = py.font.Font("resources/fonts/Carnevalee Freakshow.ttf", 40)
        self.timer_font = py.font.Font("resources/fonts/Carnevalee Freakshow.ttf", 70)
        self.game_duration = 90

        # Defines CONTROLS explanation
        self.controls_color_expl = (255, 255, 255)
        self.controls_color_keyb = (249, 239, 196)
        self.controls_font = py.font.SysFont('calibri', 20)
        self.controls_font_header = py.font.Font("resources/fonts/Carnevalee Freakshow.ttf", 40)
        self.controls_text = ["Controls",
                              "W, A, S and D",
                              "Move crosshair up, left, down and right",
                             "SPACEBAR",
                              "Shoot gun",
                             "ESC",
                              "Show pause screen"]
        self.controls_header = self.controls_font_header.render(self.controls_text[0], True, (self.controls_color_keyb))
        self.controls_line1 = self.controls_font.render(self.controls_text[1], True, (self.controls_color_keyb))
        self.controls_line3 = self.controls_font.render(self.controls_text[3], True, (self.controls_color_keyb))
        self.controls_line5 = self.controls_font.render(self.controls_text[5], True, (self.controls_color_keyb))

        self.controls_line2 = self.controls_font.render(self.controls_text[2], True, (self.controls_color_expl))
        self.controls_line4 = self.controls_font.render(self.controls_text[4], True, (self.controls_color_expl))
        self.controls_line6 = self.controls_font.render(self.controls_text[6], True, (self.controls_color_expl))

        # Defines GAME OBJECTIVE explanation
        self.objective_color = (255, 255, 255)
        self.objective_font = py.font.SysFont('calibri', 20)
        self.objective_font_header = py.font.Font("resources/fonts/Carnevalee Freakshow.ttf", 40)
        self.objective_text = ["Game Objective",
                              "Use your weapon and shoot as many wooden cowboys",
                              "as you can before the time runs out!",
                               "Hit a target to score 10 point, miss and lose 5 points"]
        self.objective_header = self.objective_font_header.render(self.objective_text[0], True, (249, 239, 196))
        self.objective_line1 = self.objective_font.render(self.objective_text[1], True, (self.objective_color))
        self.objective_line2 = self.objective_font.render(self.objective_text[2], True, (self.objective_color))
        self.objective_line3 = self.objective_font.render(self.objective_text[3], True, (self.objective_color))

        # Defines BUTTONS
        self.button = []
        self.button.append(PauseScreenButton(self.game.py_screen, "Start Game"))
        self.button.append(PauseScreenButton(self.game.py_screen, "Restart minigame"))
        self.button.append(PauseScreenButton(self.game.py_screen, "Go to main menu"))
        self.button_x = self.screen_center_width - (self.button[0].width / 2)

        # Defines game START, game PAUSE, game OVER
        self.game_is_started = False

        self.pause_event = py.USEREVENT + 5
        self.pause_duration = 15000
        self.game_is_paused = False
        self.game_paused_counter = 0
        self.alow_pause_time_check = False
        self.time_when_pause_start = 0
        self.pause_time_left = 15
        self.pause_label = Label(self.game.py_screen, "Paused", (249, 239, 176), 80,
                           "resources/fonts/Carnevalee Freakshow.ttf")
        self.pause_label_x = self.screen_center_width - (self.pause_label.get_width() / 2)

        self.game_end = False
        self.end_font = py.font.Font("resources/fonts/Carnevalee Freakshow.ttf", 70)
        self.end_text = "Well done!"
        self.display_end_text = self.end_font.render(self.end_text, 1, (249, 239, 176))

    def on_events(self, events):
        for event in events:
            if event.type == py.KEYUP:
                if event.key == py.K_ESCAPE:
                    if self.game_is_started:
                        if not self.game_is_paused:
                            self.pause_timer = py.time.set_timer(self.pause_event, self.pause_duration)
                            self.game_paused_counter += 1
                            self.game_is_paused = True
                            self.allow_pause_time_check = True
                        elif self.game_is_paused:
                            pass
                    elif not self.game_is_started:
                        pass
            elif event.type == py.MOUSEBUTTONDOWN:
                if self.button[0].is_clicked(self.mouse_position):
                    self.game_is_started = True
                    self.starting_timer = time.time()
                elif self.button[1].is_clicked(self.mouse_position):
                    self.game.drawer.clear()
                    Minigame_5(self.game)
                elif self.button[2].is_clicked(self.mouse_position):
                    from src.global_screens.main_menu import MainMenu
                    self.game.drawer.clear()
                    MainMenu(self.game)
            elif event.type == self.pause_event:
                self.game_is_paused = False
            elif event.type == self.reload_event:
                self.reloaded_gun = True
                py.time.set_timer(self.reload_event, 0)
            elif event.type == self.spawn_event:
                self.showing_target = True
                self.showing_target2 = True
                self.selected_location = self.target.get_location()
                self.selected_location2 = self.target.get_location()
                self.target_rect.x = self.selected_location[0]
                self.target_rect.y = self.selected_location[1]
                self.target_rect2.x = self.selected_location2[0]
                self.target_rect2.y = self.selected_location2[1]
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
        if not self.game_end:
            if not self.game_is_started: ################################################################## GAME_START
                # Displays BACKGROUND
                self.game.py_screen.blit(self.background_img, [0, 0])
                self.game.py_screen.blit(self.building_interior_img, [0, 0])
                self.game.py_screen.blit(self.building_exterior_img, [0, 0])
                self.game.py_screen.blit(self.building_shadows_img, [0, 0])
                self.game.py_screen.blit(self.dark_surface, [0, 0])

                # Displays OBJECTIVE
                self.game.py_screen.blit(self.objective_header, (465, 190))
                self.game.py_screen.blit(self.objective_line1, (465, 240))
                self.game.py_screen.blit(self.objective_line2, (465, 260))
                self.game.py_screen.blit(self.objective_line3, (465, 280))

                # Displays CONTROLS
                self.game.py_screen.blit(self.controls_header, (465, 320))
                self.game.py_screen.blit(self.controls_line1, (465, 370))
                self.game.py_screen.blit(self.controls_line2, (585, 370))
                self.game.py_screen.blit(self.controls_line3, (465, 390))
                self.game.py_screen.blit(self.controls_line4, (585, 390))
                self.game.py_screen.blit(self.controls_line5, (465, 410))
                self.game.py_screen.blit(self.controls_line6, (585, 410))

                # Displays BUTTONS
                self.button[0].render(self.mouse_position, self.button_x, 560)
                self.button[2].render(self.mouse_position, self.button_x, 640)
                py.display.update()

            elif self.game_is_started:
                # Time Tracker
                self.check_time = time.time()
                self.time_left = self.game_duration - int(self.check_time - self.starting_timer) \
                                 + int(self.game_paused_counter * (self.pause_duration / 1000))

                if self.game_is_paused: ################################################################# GAME_PAUSED
                    if self.allow_pause_time_check:
                        self.time_when_pause_start = self.time_left
                    elif not self.allow_pause_time_check:
                        pass

                    self.allow_pause_time_check = False
                    self.pause_time_left = (self.pause_duration/1000)-(self.time_when_pause_start-self.time_left)

                    # Displays BACKGROUND images
                    self.game.py_screen.blit(self.background_img, [0, 0])
                    self.game.py_screen.blit(self.building_interior_img, [0, 0])
                    self.game.py_screen.blit(self.building_exterior_img, [0, 0])
                    self.game.py_screen.blit(self.building_shadows_img, [0, 0])
                    self.game.py_screen.blit(self.dark_surface, [0, 0])

                    # Displays 'Paused' and 'Ends in # secs' with background
                    self.pause_label.render(self.pause_label_x, 25)
                    self.pause_time_label = Label(self.game.py_screen,
                                                  "Ends in " + str(int(self.pause_time_left)) + " secs",
                                                  (255, 255, 255), 40, "resources/fonts/Carnevalee Freakshow.ttf")
                    self.pause_time_label_x = self.screen_center_width - (self.pause_time_label.get_width() / 2)
                    self.pause_time_label.render(self.pause_time_label_x, 100)

                    # Displays OBJECTIVE
                    self.game.py_screen.blit(self.objective_header, (465, 190))
                    self.game.py_screen.blit(self.objective_line1, (465, 240))
                    self.game.py_screen.blit(self.objective_line2, (465, 260))
                    self.game.py_screen.blit(self.objective_line3, (465, 280))

                    # Displays CONTROLS
                    self.game.py_screen.blit(self.controls_header, (465, 320))
                    self.game.py_screen.blit(self.controls_line1, (465, 370))
                    self.game.py_screen.blit(self.controls_line2, (585, 370))
                    self.game.py_screen.blit(self.controls_line3, (465, 390))
                    self.game.py_screen.blit(self.controls_line4, (585, 390))
                    self.game.py_screen.blit(self.controls_line5, (465, 410))
                    self.game.py_screen.blit(self.controls_line6, (585, 410))

                    # Displays BUTTONS
                    self.button[0].render(self.mouse_position, self.button_x, 1300) # prevents pressing
                    self.button[1].render(self.mouse_position, self.button_x, 560)
                    self.button[2].render(self.mouse_position, self.button_x, 640)

                    py.display.update()

                if not self.game_is_paused: ############################################################# GAME_RUNNING
                    if self.time_left > 0:
                        # Renders buttons outside of screen while game is running
                        self.button[0].render(self.mouse_position, self.button_x, 1300)
                        self.button[1].render(self.mouse_position, self.button_x, 1300)
                        self.button[2].render(self.mouse_position, self.button_x, 1300)

                        # Displays BACKGROUND and BUILDINGS interior
                        self.game.py_screen.blit(self.background_img, [0, 0])
                        self.game.py_screen.blit(self.building_interior_img, [0, 0])

                        # Displays TARGET
                        if self.showing_target:
                            py.draw.rect(self.game.py_screen, [0, 0, 0], self.target_rect)
                            self.game.py_screen.blit(self.target_img, self.target_rect)

                        if self.showing_target2:
                            py.draw.rect(self.game.py_screen, [0, 0, 0], self.target_rect2)
                            self.game.py_screen.blit(self.target_img, self.target_rect2)

                        # Displays BUILDINGS exterior
                        self.game.py_screen.blit(self.building_exterior_img, [0, 0])

                        # Displays BUILDINGS shadows
                        self.game.py_screen.blit(self.building_shadows_img, [0, 0])

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

                        # Displays SCORE and TIME
                        self.display_score = self.score_font.render("Score: ", 1, (249, 239, 176))
                        self.display_score_count = self.score_count_font.render(str(self.score), 1, (255, 255, 255))
                        self.game.py_screen.blit(self.display_score, (880, 10))
                        self.game.py_screen.blit(self.display_score_count, (900, 50))

                        self.display_game_time = self.time_font.render("Time left:", 1, (249, 239, 176))
                        self.display_game_time2 = self.timer_font.render(str(self.time_left), 1, (255, 255, 255))
                        self.display_game_time3 = self.time_font.render("sec.", 1, (249, 239, 176))
                        self.game.py_screen.blit(self.display_game_time, (290, 10))
                        self.game.py_screen.blit(self.display_game_time2, (305, 50))
                        self.game.py_screen.blit(self.display_game_time3, (365, 70))

                        # Displays GUN STATUS
                        if self.gun_status_display:
                            self.gun_status_text = self.gun_status_font.render(self.gun_text_string,
                                                                               1, self.gun_text_color)
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
                        self.collidecheck2 = self.crosshair_rect.colliderect(self.target_rect2)

                        if self.collidecheck or self.collidecheck2:
                            self.game.py_screen.blit(self.crosshair_collide_img, self.crosshair_rect)
                        elif not self.collidecheck or self.collidecheck2:
                            self.game.py_screen.blit(self.crosshair_img, self.crosshair_rect)

                    if self.time_left <= 0:
                        self.game_end = True

        if self.game_end: ################################################################################# GAME_END
            # Displays BACKGROUND images
            self.game.py_screen.blit(self.background_img, [0, 0])
            self.game.py_screen.blit(self.building_interior_img, [0, 0])
            self.game.py_screen.blit(self.building_exterior_img, [0, 0])
            self.game.py_screen.blit(self.building_shadows_img, [0, 0])
            self.game.py_screen.blit(self.dark_surface, [0, 0])

            # Displays SCORE and END text
            self.display_score = self.score_font.render("Score: ", 1, (249, 239, 176))
            self.display_score_count = self.score_count_font.render(str(self.score), 1, (255, 255, 255))
            self.game.py_screen.blit(self.display_score, (600, 350))
            self.game.py_screen.blit(self.display_score_count, (610, 380))
            self.game.py_screen.blit(self.display_end_text, (510, 250))

            # Displays TARGETS hit
            self.display_targets_hit = self.score_font.render("You hit", 1, (249, 239, 176))
            self.display_targets_hit_count = self.score_count_font.render(str(self.target_counter), 1, (255, 255, 255))
            self.display_targets_hit2 = self.score_font.render("times", 1, (249, 239, 176))
            self.game.py_screen.blit(self.display_targets_hit, (200, 350))
            self.game.py_screen.blit(self.display_targets_hit_count, (250, 380))
            self.game.py_screen.blit(self.display_targets_hit2, (220, 450))

            # Displays TARGETS missed
            self.display_targets_missed= self.score_font.render("You missed", 1, (249, 239, 176))
            self.display_targets_missed_count = self.score_count_font.render(str(self.miss_counter), 1, (255, 255, 255))
            self.display_targets_missed2 = self.score_font.render("times", 1, (249, 239, 176))
            self.game.py_screen.blit(self.display_targets_missed, (900, 350))
            self.game.py_screen.blit(self.display_targets_missed_count, (950, 380))
            self.game.py_screen.blit(self.display_targets_missed2, (930, 450))

            # Displays BUTTONS
            self.button[0].render(self.mouse_position, self.button_x, 1300) # y coord avoids pressing
            self.button[1].render(self.mouse_position, self.button_x, 560)
            self.button[2].render(self.mouse_position, self.button_x, 640)
            py.display.update()
        py.display.update()
        return

    def handle_mouse_input(self, mouse):
        return

    def handle_key_input(self, keys):
        if keys[py.K_w] and keys[py.K_s]:
            pass
        elif keys[py.K_w]:
            self.crosshair_rect.move_ip(0, -self.crosshair_speed)
        elif keys[py.K_s]:
                self.crosshair_rect.move_ip(0, self.crosshair_speed)

        if keys[py.K_a] and keys[py.K_d]:
            pass
        elif keys[py.K_a]:
            self.crosshair_rect.move_ip(-self.crosshair_speed, 0)
        elif keys[py.K_d]:
            self.crosshair_rect.move_ip(self.crosshair_speed, 0)

        if keys[py.K_SPACE]:
            if not self.game_end:
                if self.game_is_started:
                    if not self.game_is_paused:
                        if self.reloaded_gun:
                            py.mixer.music.play()
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
                                py.mixer.music.play(0)
                                self.score += 10
                                self.target_counter += 1

                            if self.collidecheck2:
                                self.reloaded_gun = False
                                self.showing_target2 = False
                                self.gun_status = 1
                                self.gun_shot_succes = True
                                self.gun_status_display = True
                                self.target_rect2.x = 1280
                                py.time.set_timer(self.reload_event, self.reload_speed)
                                py.time.set_timer(self.gun_shot_disappear_event, self.time_till_shot_disappear)
                                py.time.set_timer(self.gun_status_event, self.time_till_gun_status_text_disappears)
                                self.score += 10
                                self.target_counter += 1

                            if not self.collidecheck and not self.collidecheck2:
                                self.reloaded_gun = False
                                self.gun_status = 2
                                self.gun_shot_succes = True
                                self.gun_status_display = True
                                py.time.set_timer(self.reload_event, self.reload_speed)
                                py.time.set_timer(self.gun_shot_disappear_event, self.time_till_shot_disappear)
                                py.time.set_timer(self.gun_status_event, self.time_till_gun_status_text_disappears)
                                self.score -= 5
                                self.miss_counter += 1
                        if not self.reloaded_gun:
                            pass
                    if self.game_is_paused:
                        pass
                if self.game_is_started:
                    pass
            if self.game_end:
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
            self.crosshair_speed = 30
        elif keys[py.K_7]:
            self.crosshair_speed = 35 # default
        elif keys[py.K_8]:
            self.crosshair_speed = 40
        elif keys[py.K_9]:
            self.crosshair_speed = 20
        elif keys[py.K_0]:
            self.crosshair_speed = 10
        return

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position
        return

class PauseScreenButton(ImageButton):
    def __init__(self, screen, text):
        button_file = "resources/graphics/button_background_v3.png"
        text_color = (255, 255, 255)
        text_color_hover = (249, 239, 176)
        text_size = 50
        button_width = 360
        button_height = 70
        super().__init__(screen, button_file, text, text_color, text_color_hover, text_size,
                         button_width, button_height)