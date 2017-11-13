from abc import ABCMeta, abstractmethod
from game import Game

class MinigameBase(object):
    """ Abstract minigame base class used for all the minigames """
    __metaclass__ = ABCMeta

    def __init__(self, instance: Game):
        self.instance = instance

    @abstractmethod
    def handleMouseClickInput(self, input):
        """ Gets called when a mouse button has been pressed """
        pass

    @abstractmethod
    def handleKeyboardInput(self, input):
        """ Gets called when a key is pressed """
        pass