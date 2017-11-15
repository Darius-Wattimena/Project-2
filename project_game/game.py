""" Game module """
import pygame as py, logging
from helper.drawer import Drawer

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
        while self.running:
            self.clock.tick(30)
            self.process_events(py.event.get())
            self.render()

    def quit(self):
        """ Quit the game. """
        py.quit()
            
    def process_events(self, events):
        """ Process all the events we get from pygame. """
        self.handle_key_press()

        for event in events:
            event_type = event.type
            if event_type == py.QUIT:
                self.running = False
                self.quit()
            elif event_type == py.MOUSEBUTTONDOWN:
                self.handle_mouse_press(event)
                      
    
    def handle_mouse_press(self, event):
        """ Get called when a mouse button is pressed. """
        if self.minigame is not None:
            self.minigame.handleMouseClickInput(event)
        self.logger.info(event.button)

    def handle_key_press(self):
        """ Get called when a key is pressed. """
        keys = py.key.get_pressed()
        if self.minigame is not None:
            self.minigame.handleKeyboardInput(keys)
        
        image = self.drawer.items[1]
        image2 = self.drawer.items[1]
        if keys[py.K_LEFT]:
            image.move(-1, 0)
        if keys[py.K_RIGHT]:
            image.move(1, 0)
        if keys[py.K_UP]:
            image.move(0, -1)
        if keys[py.K_DOWN]:
            image.move(0, 1)

    def setup_window(self):
        """ Setup the window. """
        self.screen = py.display.set_mode([self.screen_x, self.screen_y])
        py.display.set_caption(self.name)

    def render(self):
        """ Render all the images given to the drawer on the screen. """
        self.drawer.draw_canvas()
        py.display.update()
