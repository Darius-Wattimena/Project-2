from abc import ABCMeta

from .game_object_group import GameObjectGroup


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
        if side == 1:
            return self.object_group.distance_to_above(self)
        elif side == 2:
            return self.object_group.distance_to_right(self)
        elif side == 3:
            return self.object_group.distance_to_below(self)
        else:
            return self.object_group.distance_to_left(self)
