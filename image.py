class Image:
    """ Image class used to handle """
    def __init__(self, data, rect):
        self.data = data
        self.rect = rect

    def clone(self, position_x=None, position_y=None):
        """ Return a clone of this image with a new image rectangle """
        if position_x is not None and position_y is not None:
            cloneRect = self.rect.move(position_x, position_y)
        else:
            cloneRect = self.rect.move(0, 0)
        clonedImage = Image(self.data, cloneRect)
        return clonedImage

    def move(self, x, y):
        """ Move this image to a new position """
        self.rect.move_id(x, y)
