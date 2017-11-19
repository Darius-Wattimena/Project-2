from .image import Image
from .game_object_group import GameObjectGroup
from abc import ABCMeta, abstractmethod

class GameObject:

    __metaclass__ = ABCMeta

    def __init__(self, object_group: GameObjectGroup, velocity=1, solid=False, rect=None):
        object_group.add_object(self)
        self.object_group = object_group
        self.velocity = velocity
        self.solid = solid
        self.rect = rect
        self.initialise()

    def initialise(self):
        """ Use this method for adding an image or init more stuff after the default init """
        return

    def set_velocity(self, velocity):
        self.velocity = velocity

    def is_solid(self, solid):
        self.solid = solid

    def set_rect(self, rect):
        self.rect = rect

    def distance_to_first_solid_object(self, side):
        if(side == 1):
            return self.object_group.distance_to_above(self)
        elif(side == 2):
            return self.object_group.distance_to_right(self)
        elif(side == 3):
            return self.object_group.distance_to_below(self)
        else:
            return self.object_group.distance_to_left(self)

    def on_event(self, events):
        return

    def on_update(self):
        """ This will be called by the drawer every frame before the render """
        return

    @abstractmethod
    def on_render(self):
        """ This will be called by the drawer every frame, only use this method to handle rendering to the screen """
        pass
