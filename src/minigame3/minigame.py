import pygame as py

from src.helper.label import Label
from src.helper.screen_base import ScreenBase
from src.minigame1.fight import PauseScreenButton
from src.minigame1.ui.header_label import HeaderLabel
from src.minigame1.ui.text_label import TextLabel
from src.minigame3.enemy import Enemy


class Minigame_3(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.enemy_is_spawned = True
        self.enemy_is_moving = True
        self.player_is_collided = False
        self.coyote_is_spawned = True
        self.coyote_is_moving = True
        self.start_game = False
        self.end_game = False
        self.win_game = False
        self.groundcolor = (240, 230, 140)
        self.skycolor = (20, 20, 255)

        self.groundrect = py.Rect([0, 250], [1280, 720])
        self.skyrect = py.Rect([0, 0], [1280, 250])

        self.beginning_lives = 2
        self.lives = self.beginning_lives
        self.player_start_pos = [640, 650]
        self.coyote_start_pos = [640, 250]

        self.player()
        self.enemy()
        self.coyote()

        self.dark_surface = py.Surface((1280, 720))
        self.dark_surface.set_alpha(170)

        self.objective_text = ["Game Objective",
                               "Reach the coyote, and capture him to win the game!",
                               "Watch out for the obstacles, though. They take lives from you!",
                               "Once you reach 0 lives, you're game over!"]
        self.objective_label_header = HeaderLabel(self.game.py_screen, self.objective_text[0])
        self.objective_label_text_1 = TextLabel(self.game.py_screen, self.objective_text[1])
        self.objective_label_text_2 = TextLabel(self.game.py_screen, self.objective_text[2])
        self.objective_label_text_3 = TextLabel(self.game.py_screen, self.objective_text[3])

        self.controls_text = ["Controls",
                              "Move left and right with the A and D keys.",
                              "Move faster and slower with the W and S keys.",
                              "Capture the coyote with the space bar!"]

        self.controls_label_header = HeaderLabel(self.game.py_screen, self.controls_text[0])
        self.controls_label_text_1 = TextLabel(self.game.py_screen, self.controls_text[1])
        self.controls_label_text_2 = TextLabel(self.game.py_screen, self.controls_text[2])
        self.controls_label_text_3 = TextLabel(self.game.py_screen, self.controls_text[3])

        self.btn = []
        self.btn.append(PauseScreenButton(game.py_screen, "Start"))
        self.btn.append(PauseScreenButton(game.py_screen, "Back"))

        self.death_text = ["Oh no, you died!",
                           "No worries! press 'Start' to try again!",
                           "Or press 'Back' to play another game!"]

        self.death_label_header = HeaderLabel(self.game.py_screen, self.death_text[0])
        self.death_label_text_1 = TextLabel(self.game.py_screen, self.death_text[1])
        self.death_label_text_2 = TextLabel(self.game.py_screen, self.death_text[2])

        self.win_text = ["Congratulations!",
                         "You caught the coyote troubling the townspeople.",
                         "To play again, press 'Start'",
                         "to go back to the menu, press 'back'"]

        self.win_label_header = HeaderLabel(self.game.py_screen, self.win_text[0])
        self.win_label_text_1 = TextLabel(self.game.py_screen, self.win_text[1])
        self.win_label_text_2 = TextLabel(self.game.py_screen, self.win_text[2])
        self.win_label_text_3 = TextLabel(self.game.py_screen, self.win_text[3])

        screen_center_width = self.game.py_screen.get_width() / 2
        self.button_x = screen_center_width - (self.btn[0].width / 2)

        self.spawn_event = py.USEREVENT + 1
        self.time_between_spawn = 3000
        py.time.set_timer(self.spawn_event, self.time_between_spawn)

        self.move_event = py.USEREVENT + 2
        self.time_between_movement = 5
        py.time.set_timer(self.move_event, self.time_between_spawn)

        self.collide_event = py.USEREVENT + 3

        self.coyote_event = py.USEREVENT + 4

        self.coyote_move_event = py.USEREVENT + 5
        self.time_between_coyote_movement = 200
        py.time.set_timer(self.coyote_move_event, self.time_between_coyote_movement)

        self.lives_label = Label(self.game.py_screen, "Current Lives: " + str(self.lives), [0, 0, 0], 50)

    def start(self):
        self.end_game = False
        self.win_game = False
        self.start_game = True

    def reset(self):
        # Reset lives and the label
        self.lives = self.beginning_lives
        self.lives_label.text = "Current Lives: " + str(self.lives)

        # Reset position of player and the coyote
        self.player_rect.x = self.player_start_pos[0]
        self.player_rect.y = self.player_start_pos[1]
        self.coyote_location = self.coyote_start_pos
        self.coyote_rect.x = self.coyote_start_pos[0]
        self.coyote_rect.y = self.coyote_start_pos[1]

        # Start the minigame
        self.start()


    def player(self):
        player_width = 100
        player_height = 100
        self.player_image = py.image.load("resources/graphics/minigame_3/cowboy.png")
        # Resize je foto omdat de photo kleiner is dan de player rect
        self.player_image = py.transform.scale(self.player_image, [player_width, player_height])
        self.player_rect = py.Rect(self.player_start_pos, [player_width, player_height])
        self.lives = self.beginning_lives

    def enemy(self):
        enemy_width = 100
        enemy_height = 100
        self.enemy_image = py.image.load("resources/graphics/minigame_3/cactus.png")
        # Resize je foto omdat de photo kleiner is dan de enemy rect
        self.enemy_image = py.transform.scale(self.enemy_image, [enemy_width, enemy_height])
        self.enemy_location = Enemy().get_location()
        self.enemy_rect = py.Rect(self.enemy_location, [enemy_width, enemy_height])

    def coyote(self):
        coyote_width = 100
        coyote_height = 100
        self.coyote_image = py.image.load("resources/graphics/minigame_3/coyote.png")
        self.coyote_image = py.transform.scale(self.coyote_image, [coyote_width, coyote_height])
        self.coyote_location = self.coyote_start_pos
        self.coyote_rect = py.Rect(self.coyote_location, [coyote_width, coyote_height])

    def on_events(self, events):
        for event in events:
            if self.start_game is True:
                if event.type == self.spawn_event:
                    self.enemy_is_spawned = True
                    self.selected_location = Enemy().get_location()
                    self.enemy_rect.x = self.selected_location[0]
                    self.enemy_rect.y = self.selected_location[1]
                    self.player_is_collided = False
                if event.type == self.move_event:
                    self.enemy_is_moving = True
                    self.enemy_rect.move_ip(0, 2)
                    py.time.set_timer(self.move_event, self.time_between_movement)
                if event.type == self.collide_event:
                    collision = self.player_rect.colliderect(self.enemy_rect)
                    if collision:
                        if self.player_is_collided is False:
                            if self.lives >= 1:
                                self.lives -= 1
                                self.player_is_collided = True
                                self.lives_label.text = "Current Lives: " + str(self.lives)

                            # End the game when 0 lives are left
                            if self.lives == 0:
                                self.end_game = True
                                self.start_game = False
                if event.type == self.coyote_event:
                    self.coyote_is_spawned = True
                self.coyote_selected_location = self.coyote_location
                if event.type == self.coyote_move_event:
                    self.coyote_is_moving = True
                    self.coyote_rect.move_ip(0, 1)
            else:
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.btn[0].is_clicked(self.mouse_position):
                        if self.end_game is False:
                            self.start()
                        else:
                            self.reset()
                    elif self.btn[1].is_clicked(self .mouse_position):
                        from src.global_screens.pick_minigame import PickMinigame
                        self.game.drawer.clear()
                        PickMinigame(self.game)

    def on_update(self):
        # Elke frame roepen wij deze event aan en kijken we of er collision is
        py.event.post(py.event.Event(self.collide_event))

    def on_render(self):
        if self.start_game:
            self.game.drawer.draw_canvas()
            py.draw.rect(self.game.py_screen, self.groundcolor, self.groundrect)
            py.draw.rect(self.game.py_screen, self.skycolor, self.skyrect)
            self.game.py_screen.blit(self.player_image, self.player_rect)

            if self.enemy_is_spawned is True:
                py.draw.rect(self.game.py_screen, [240, 230, 140], self.enemy_rect)
                self.game.py_screen.blit(self.enemy_image, self.enemy_rect)
            if self.enemy_is_moving is True:
                py.draw.rect(self.game.py_screen, [240, 230, 140], self.enemy_rect)
                self.game.py_screen.blit(self.enemy_image, self.enemy_rect)
            if self.coyote_is_spawned is True:
                py.draw.rect(self.game.py_screen, [240, 230, 140], self.coyote_rect)
                self.game.py_screen.blit(self.coyote_image, self.coyote_rect)
            self.lives_label.render(100, 100)
        else:
            if self.end_game is False:
                self.game.drawer.draw_canvas()
                # Draw an dark surface on the screen
                self.game.py_screen.blit(self.dark_surface, [0, 0])

                # Draw objective
                self.objective_label_header.render(465, 190)
                self.objective_label_text_1.render(465, 240)
                self.objective_label_text_2.render(465, 260)
                self.objective_label_text_3.render(465, 280)

                # Draw controlls
                self.controls_label_header.render(465, 320)
                self.controls_label_text_1.render(465, 370)
                self.controls_label_text_2.render(465, 420)
                self.controls_label_text_3.render(465, 470)

                self.btn[1].render(self.mouse_position, self.button_x, 640)
                self.btn[0].render(self.mouse_position, self.button_x, 560)
            elif self.win_game is False:
                self.game.py_screen.blit(self.dark_surface, [0, 0])

                self.death_label_header.render(465, 190)
                self.death_label_text_1.render(465, 240)
                self.death_label_text_2.render(465, 260)

                self.btn[0].render(self.mouse_position, self.button_x, 560)
                self.btn[1].render(self.mouse_position, self.button_x, 640)

            elif self.win_game is True:
                self.game.py_screen.blit(self.dark_surface, [0, 0])

                self.win_label_header.render(465, 190)
                self.win_label_text_1.render(465, 240)
                self.win_label_text_2.render(465, 260)
                self.win_label_text_3.render(465, 280)

                self.btn[0].render(self.mouse_position, self.button_x, 560)
                self.btn[1].render(self.mouse_position, self.button_x, 640)

        py.display.update()

    def handle_mouse_input(self, mouse):
        return

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position

    def handle_key_input(self, keys):
        if keys[py.K_a]:
            self.player_rect.move_ip(-10, 0)
        elif keys[py.K_d]:
            self.player_rect.move_ip(10, 0)
        if keys[py.K_w]:
            self.enemy_rect.move_ip(0, 5)
            self.coyote_rect.move_ip(0, 1)
        elif keys[py.K_s]:
            self.enemy_rect.move_ip(0, -1)
            self.coyote_rect.move_ip(0, -1)
        if keys[py.K_SPACE]:
            coyote_collision = self.player_rect.colliderect(self.coyote_rect)
            if coyote_collision:
                self.lives_label.text = "You won!"
                self.win_game = True
                self.start_game = False
                self.end_game = True
        return
