import pygame as py
from drawer import Drawer

class Game:
    def __init__(self, screen_x, screen_y):
        py.init()
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.running = False
        self.minigame = None
        self.clock = py.time.Clock()

    def start(self):
        self.setupWindow()
        self.drawer = Drawer(self.screen)
        self.running = True
        while self.running:
            self.clock.tick(30)
            self.processEvents(py.event.get())

    def quit(self):
        py.quit
            
    def processEvents(self, events):
        for event in events:
            eventType = event.type

            if eventType == py.QUIT:
                self.running = False
                self.quit()
            elif eventType == py.MOUSEBUTTONDOWN:
                self.handleMousePress(eventType)
            elif eventType == py.KEYDOWN:
                self.handleKeyPress(eventType)        
    
    def handleMousePress(self, eventType):
        if self.minigame is not None:
            self.minigame.handleMouseClickInput(eventType)

    def handleKeyPress(self, eventType):
        if self.minigame is not None:
            self.minigame.handleKeyboardInput(eventType)

    def setupWindow(self):
        self.screen = py.display.set_mode([self.screen_x, self.screen_y])

    def draw(self, d: Drawer):
        d.drawCanvas()
        self.screen.update()
