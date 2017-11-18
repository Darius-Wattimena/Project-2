""" Minigame base module """

from abc import ABCMeta, abstractmethod

class MinigameBase(object):
    """ Abstract minigame base class used for all the minigames """
    __metaclass__ = ABCMeta

    def __init__(self, game):
        self.game = game

    @abstractmethod
    def handle_mouse_position(self, mouse_position):
        """ Gets called every frame giving the current mouse_position """
        pass

    @abstractmethod
    def handle_mouse_input(self, event):
        """ Gets called when a mouse button is being hold """
        pass

    @abstractmethod
    def handle_mouse_down(self, event):
        """ Gets called when a mouse button is pressed """
        pass

    @abstractmethod
    def handle_mouse_up(self, event):
        """ Gets called when a mouse button is lifted """
        pass

    @abstractmethod
    def handle_keyboard_input(self, keys):
        """ Gets called when a key is being hold """
        pass

    @abstractmethod
    def handle_keyboard_down(self, event):
        """ Gets called when a key is pressed """
        pass

    @abstractmethod
    def handle_keyboard_up(self, event):
        """ Gets called when a key is lifted """
        pass
