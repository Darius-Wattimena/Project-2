""" Game module """
import pygame as py, logging
from .helper.drawer import Drawer
from .helper.singleton import Singleton
from .global_screens.main_menu import MainMenu


@Singleton
class Game:
    """ This class is where the start and stop the game and where we place the game loop. """

    def __init__(self):
        self.enable_logging()
        self.running = False
        self.minigame = None
        self.drawer = None
        self.clock = py.time.Clock()

    def enable_logging(self):
        self.logger = logging.getLogger('scope.name')
        self.logger.setLevel(logging.DEBUG)

        file_log_handler = logging.FileHandler('logfile.log')
        self.logger.addHandler(file_log_handler)

        stderr_log_handler = logging.StreamHandler()
        self.logger.addHandler(stderr_log_handler)

        # nice output format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_log_handler.setFormatter(formatter)
        stderr_log_handler.setFormatter(formatter)

    def start(self, py_screen):
        """ Start the game. """
        self.py_screen = py_screen
        self.drawer = Drawer.Instance()
        self.drawer.set_screen(self.py_screen)
        self.screen = MainMenu(self)
        self.running = True
        self.game_loop()

    def game_loop(self):
        while self.running:
            self.clock.tick(30)
            self.screen.handle_key_input(py.key.get_pressed())
            self.screen.handle_mouse_input(py.mouse.get_pressed())
            self.screen.handle_mouse_position(py.mouse.get_pos())
            self.handle_events(py.event.get())
            if self.running:
                self.screen.on_update()
                self.screen.on_render()

    def handle_events(self, events):
        for event in events:
            if event.type == py.QUIT:
                self.quit()
        self.screen.on_events(events)

    def quit(self):
        """ Quit the game. """
        self.running = False
        py.quit()

    def set_screen(self, screen):
        self.screen = screen
