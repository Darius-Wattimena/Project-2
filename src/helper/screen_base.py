""" Minigame base module """

from abc import ABCMeta, abstractmethod

class ScreenBase(object):
    """ Abstract minigame base class used for all the minigames """
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_events(self, events):
        """ Gets called on an event """
        pass

    @abstractmethod
    def on_update(self):
        """ Gets called every frame before the render """
        pass

    @abstractmethod
    def on_render(self):
        """ Gets called on an event used only to render to the screen """
        pass

    def set_screen(self, screen):
        self.screen = screen

    @abstractmethod
    def handle_mouse_position(self, mouse_position):
        """ Gets called every frame giving the current mouse_position """
        pass

    @abstractmethod
    def handle_mouse_input(self, event):
        """ Gets called when a mouse button is being hold """
        pass

    @abstractmethod
    def handle_keyboard_input(self, keys):
        """ Gets called when a key is being hold """
        pass