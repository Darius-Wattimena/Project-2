""" Game module """
import pygame as py, logging
from .helper.drawer import Drawer
from .minigame1.minigame import Minigame_1

class Game:
    """ Game class where every input is handled, screen is being rendered and the current minigame is going to be managed. """

    def __init__(self, name, screen_x, screen_y):
        py.init()
        self.name = name
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.running = False
        self.minigame = None
        self.drawer = None
        self.clock = py.time.Clock()
        self.enable_logging()

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
        self.setup_window()
        self.drawer = Drawer(self.screen)
        self.drawer.add_image("pygame_tiny.png")
        self.drawer.add_image("1327.jpg")
        self.running = True
        self.start_minigame(1)
        while self.running:
            self.clock.tick(30)
            self.process_events(py.event.get())
            self.render()

    def start_minigame(self, number):
        minigames = {
            1 : self.start_minigame_1,
            2 : self.start_minigame_2,
            3 : self.start_minigame_3,
            4 : self.start_minigame_4,
            5 : self.start_minigame_5,
        }
        minigames[number]()
    
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

    def quit(self):
        """ Quit the game. """
        py.quit()
            
    def process_events(self, events):
        """ Process all the events we get from pygame. """
        self.handle_key_input()
        self.handle_mouse_input()

        for event in events:
            event_type = event.type
            if event_type == py.QUIT:
                self.running = False
                self.quit()
            elif event_type == py.MOUSEBUTTONUP:
                self.handle_mouse_release(event)
            elif event_type == py.MOUSEBUTTONDOWN:
                self.handle_mouse_press(event)
            elif event_type == py.KEYDOWN:
                self.handle_key_press(event)
            elif event_type == py.KEYUP:
                self.handle_key_release(event)

    def handle_mouse_input(self):
        """ Handle mouse motion """
        mouse_position = py.mouse.get_pos()
        if self.minigame is not None:
            self.minigame.handle_mouse_position(mouse_position)       
    
    def handle_mouse_press(self, event):
        """ Get called when a mouse button is pressed. """
        if self.minigame is not None:
            self.minigame.handle_mouse_down(event)

    def handle_mouse_release(self, event):
        """ Get called when a mouse button is released. """
        if self.minigame is not None:
            self.minigame.handle_mouse_up(event)

    def handle_key_input(self):
        """ Handle all the pressed keys.  """
        keys = py.key.get_pressed()
        if self.minigame is not None:
            self.minigame.handle_keyboard_input(keys)

    def handle_key_press(self, event):
        """ Get called when a key is pressed. """
        if self.minigame is not None:
            self.minigame.handle_keyboard_down(event)

    def handle_key_release(self, event):
        """ Get called when a key is released. """
        if self.minigame is not None:
            self.minigame.handle_keyboard_up(event)

    def setup_window(self):
        """ Setup the window. """
        self.screen = py.display.set_mode([self.screen_x, self.screen_y])
        py.display.set_caption(self.name)

    def render(self):
        """ Render all the images given to the drawer on the screen. """
        self.drawer.draw_canvas()
        py.display.update()
