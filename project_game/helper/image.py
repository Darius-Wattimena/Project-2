""" Image module """

class Image:
    """ Image class used to handle """
    def __init__(self, data, rect):
        self.data = data
        self.rect = rect
        self.current_x = 0
        self.current_y = 0

    def clone(self, position_x=0, position_y=0):
        """ Return a clone of this image with a new image rectangle """
        clone_rect = self.rect.move(position_x, position_y)
        cloned_image = Image(self.data, clone_rect)
        return cloned_image

    def move(self, x, y):
        """ Move this image to a new position """
        self.rect.move_ip(x,y)

    def is_collided(self, other):
        """ Checks if there is collision """
        self.rect.colliderect(other.rect)
