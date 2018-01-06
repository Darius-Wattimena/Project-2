from src.helper.image_button import ImageButton
from src.helper.label import Label
from src.helper.screen_base import ScreenBase
from src.helper.game_object_group import GameObjectGroup
from src.minigame1.ai import AI, AIState
from src.minigame1.custom_event import AIEvent
from src.minigame1.ui.header_label import HeaderLabel
from src.minigame1.ui.text_label import TextLabel
from src.minigame1.health_bar import HealthBar
from .player import Player, PlayerState
import pygame as py


class Fight(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.game_object_group = GameObjectGroup()
        self.game.drawer.clear()
        self.game.drawer.add_image("resources/graphics/minigame_1/background.png")
        debug = self.game.DEBUG
        self.mouse_position = None
        self.player = Player(self.game_object_group, self.game.py_screen, debug)
        self.ai = AI(self.game_object_group, self.game.py_screen, debug)
        self.first = True
        self.passed_time = 0
        self.player_health_bar = HealthBar(self.game.py_screen, 10, 10, True)
        self.ai_health_bar = HealthBar(self.game.py_screen, 860, 10, False)
        self.winner_label = Label(self.game.py_screen, "", [249, 239, 196], 100, font="resources/fonts/Carnevalee Freakshow.ttf")
        self.fight_paused_label = Label(self.game.py_screen, "Bar Fight", [249, 239, 196], 100, font="resources/fonts/Carnevalee Freakshow.ttf")
        self.fight_paused = True

        self.dark_surface = py.Surface((1280, 720))
        self.dark_surface.set_alpha(170)

        self.objective_text = ["Game Objective",
                               "Use your fists to fight against",
                               "your opponent and win",
                               "by beating him to 0 hp!"]
        self.objective_label_header = HeaderLabel(self.game.py_screen, self.objective_text[0])
        self.objective_label_text_1 = TextLabel(self.game.py_screen, self.objective_text[1])
        self.objective_label_text_2 = TextLabel(self.game.py_screen, self.objective_text[2])
        self.objective_label_text_3 = TextLabel(self.game.py_screen, self.objective_text[3])

        self.controls_text = ["Controls",
                              "A and D",
                              "Move your fighter to the left and right",
                              "J",
                              "Punch",
                              "K",
                              "Block",
                              "ESC",
                              "Show pause screen"]

        self.controls_label_header = HeaderLabel(self.game.py_screen, self.controls_text[0])
        self.controls_label_text_1 = TextLabel(self.game.py_screen, self.controls_text[1])
        self.controls_label_text_2 = TextLabel(self.game.py_screen, self.controls_text[2])
        self.controls_label_text_3 = TextLabel(self.game.py_screen, self.controls_text[3])
        self.controls_label_text_4 = TextLabel(self.game.py_screen, self.controls_text[4])
        self.controls_label_text_5 = TextLabel(self.game.py_screen, self.controls_text[5])
        self.controls_label_text_6 = TextLabel(self.game.py_screen, self.controls_text[6])
        self.controls_label_text_7 = TextLabel(self.game.py_screen, self.controls_text[7])
        self.controls_label_text_8 = TextLabel(self.game.py_screen, self.controls_text[8])

        self.btn = []
        self.btn.append(PauseScreenButton(game.py_screen, "Start"))
        self.btn.append(PauseScreenButton(game.py_screen, "Back"))

        screen_center_width = self.game.py_screen.get_width() / 2
        self.button_x = screen_center_width - (self.btn[0].width / 2)

        self.ai_event = AIEvent(self.ai, self.player)
        py.time.set_timer(self.ai_event.type, 600)

    def on_events(self, events):
        for event in events:
            if event.type == py.KEYDOWN:
                if not self.player.punch_animation_running:
                    if event.key == py.K_j:
                        self.player.punching = True
                if event.key == py.K_ESCAPE:
                    self.handle_escape()
            elif event.type == py.MOUSEBUTTONDOWN:
                if self.btn[0].is_clicked(self.mouse_position):
                    self.fight_paused = False
                elif self.btn[1].is_clicked(self.mouse_position):
                    from src.global_screens.pick_minigame import PickMinigame
                    self.game.drawer.clear()
                    PickMinigame(self.game)
            elif event.type == self.ai_event.type:
                self.ai_event.execute()
            elif event.type == py.USEREVENT + 2:
                self.player.state = PlayerState.IDLE
                self.ai.state = AIState.IDLE
                event.instance.execute(self)
        return

    def handle_escape(self):
        if self.winner_label.text != "":
            from src.global_screens.pick_minigame import PickMinigame
            self.game.drawer.clear()
            PickMinigame(self.game)
        else:
            self.player.state = PlayerState.IDLE
            self.ai.state = AIState.IDLE
            self.fight_paused = not self.fight_paused

    def on_render(self):
        self.player.needs_new_rendering()
        self.ai.needs_new_rendering()
        if not self.fight_paused:
            self.game.drawer.draw_canvas()
            self.player.on_render()
            self.ai.on_render()

            if self.player.is_hitting_punch(self.ai):
                self.ai.on_hit(self.player)
            if self.ai.is_hitting_punch(self.player):
                self.player.on_hit(self.ai)

            self.ai_health_bar.on_render(self.ai)
            self.player_health_bar.on_render(self.player)
        elif self.fight_paused:
            # Draw the main stuff on the screen
            self.game.drawer.draw_canvas()
            self.ai_health_bar.on_render(self.ai)
            self.player_health_bar.on_render(self.player)

            # Draw the paused animation of the player and ai
            self.player.paused()
            self.ai.paused()

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
            self.controls_label_text_2.render(585, 370)
            self.controls_label_text_3.render(465, 390)
            self.controls_label_text_4.render(585, 390)
            self.controls_label_text_5.render(465, 410)
            self.controls_label_text_6.render(585, 410)
            self.controls_label_text_7.render(465, 430)
            self.controls_label_text_8.render(585, 430)
            self.btn[1].render(self.mouse_position, self.button_x, 640)

            if self.player.won_fight is not None:
                self.winner_label.render(430, 70)
            else:
                self.btn[0].render(self.mouse_position, self.button_x, 560)
                self.fight_paused_label.render(450, 70)
        py.display.update()

    def on_update(self):
        if self.player.won_fight is not None:
            self.fight_paused = True
        else:
            self.passed_time += self.game.clock.get_time()
            if self.passed_time > 500:
                # self.ai.on_update(self.player.state == PlayerState.BLOCKING)
                self.passed_time = 0

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position

    def handle_mouse_input(self, event):
        return

    def handle_key_input(self, keys):
        if not self.fight_paused:
            self.player.blocking = False
            if keys[py.K_k] and not self.player.punch_animation_running:
                self.player.set_state(PlayerState.BLOCKING)
            elif keys[py.K_d]:
                self.player.set_state(PlayerState.WALKING)
            elif keys[py.K_a]:
                self.player.set_state(PlayerState.WALKING_REVERSE)
            else:
                self.player.set_state(PlayerState.IDLE)
        return


class PauseScreenButton(ImageButton):
    def __init__(self, screen, text):
        button_file = "resources/graphics/button_background_v3.png"
        text_color = [249, 239, 196]
        text_color_hover = [0, 0, 0]
        text_size = 45
        button_width = 350
        button_height = 70
        super().__init__(screen, button_file, text, text_color, text_color_hover, text_size,
                         button_width, button_height)
