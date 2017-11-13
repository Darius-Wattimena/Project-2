import pygame
from Drawer import Drawer

class Game:
    def __init__(self, screen_x, screen_y):
        self.screen_x = screen_x
        self.screen_y = screen_y
        pygame.init()

    def startGame(self):
        self.setupWindow()

    def quitGame(self):
        pygame.quit()

    def setupWindow(self):
        pygame.display.set_mode([self.screen_x, self.screen_y])

    def draw(self, drawer: Drawer):
        drawer.drawCanvas()