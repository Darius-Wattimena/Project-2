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
        self.clock = py.time.Clock()
        self.enableLogging()

    def enableLogging(self):
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
        self.setupWindow()
        self.drawer = Drawer(self.screen)
        self.drawer.addImage("pygame_tiny.png")
        self.drawer.addImage("1327.jpg")
        self.running = True
        while self.running:
            self.clock.tick(30)
            self.processEvents(py.event.get())
            self.render()

    def quit(self):
        """ Quit the game. """
        py.quit()
            
    def processEvents(self, events):
        """ Process all the events we get from pygame. """
        for event in events:
            eventType = event.type
            if eventType == py.QUIT:
                self.running = False
                self.quit()
            elif eventType == py.MOUSEBUTTONDOWN:
                self.handleMousePress(event)
            elif eventType == py.KEYDOWN:
                self.handleKeyPress(event)      
    
    def handleMousePress(self, event):
        """ Get called when a mouse button is pressed. """
        if self.minigame is not None:
            self.minigame.handleMouseClickInput(event)
        self.logger.info(event.button)

    def handleKeyPress(self, event):
        """ Get called when a key is pressed. """
        if self.minigame is not None:
            self.minigame.handleKeyboardInput(event)
        self.logger.info(event.key)
        
        image = self.drawer.items[1]
        image2 = self.drawer.items[1]
        if event.key == py.K_LEFT:
            image.move(-1, 0)
        elif event.key == py.K_RIGHT:
            image.move(1, 0)
        elif event.key == py.K_UP:
            image.move(0, -1)
        elif event.key == py.K_DOWN:
            image.move(0, 1)

    def setupWindow(self):
        """ Setup the window. """
        self.screen = py.display.set_mode([self.screen_x, self.screen_y])
        py.display.set_caption(self.name)

    def render(self):
        """ Render all the images given to the drawer on the screen. """
        self.drawer.drawCanvas()
        py.display.update()
