""" Game module """
import pygame as py, logging
from .helper.drawer import Drawer
from .minigame1.minigame import Minigame_1

class Game:
    """ Game class where every input is handled, screen is being rendered and the current minigame is going to be managed. """

    def __init__(self, screen):
        self.enable_logging()
        self.screen = screen
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

    def start(self):
        """ Start the game. """
        self.drawer = Drawer.Instance()
        self.drawer.set_screen(self.screen)
        self.drawer.add_image("pygame_tiny.png")
        self.drawer.add_image("1327.jpg")
        self.running = True
        self.start_minigame(1)
        self.game_loop()
    
    def game_loop(self):
        while self.running:
            self.clock.tick(30)
            self.process_events()
            self.render()

    def start_minigame(self, number):
        minigames_dict = {
            1 : self.start_minigame_1,
            2 : self.start_minigame_2,
            3 : self.start_minigame_3,
            4 : self.start_minigame_4,
            5 : self.start_minigame_5,
        }
        minigames_dict[number]()
    
    def start_minigame_1(self):
        self.minigame = Minigame_1(self)

    def start_minigame_2(self):
        pass

    def start_minigame_3(self):
        pass

    def start_minigame_4(self):
        pass

    def start_minigame_5(self):
        pass
            
    def process_events(self):
        """ Process all the events we get from pygame. """
        self.handle_key_input()
        self.handle_mouse_input()
        events = py.event.get()

        for event in events:
            if event.type == py.QUIT:
                self.running = False
                self.quit()
            elif self.minigame is not None:
                self.minigame.on_event(event)


    def handle_key_input(self):
        """ Handle all the pressed keys.  """
        keys = py.key.get_pressed()
        if self.minigame is not None:
            self.minigame.handle_keyboard_input(keys)

    def handle_mouse_input(self):
        """ Handle mouse motion. """
        mouse_position = py.mouse.get_pos()
        if self.minigame is not None:
            self.minigame.handle_mouse_position(mouse_position)

    def update(self):
        if self.minigame is not None:
            self.minigame.update()

    def render(self):
        """ Render all the images given to the drawer on the screen. """
        self.drawer.draw_canvas()
        py.display.update()
        if self.minigame is not None:
            self.minigame.render()

    def quit(self):
        """ Quit the game. """
        py.quit()
