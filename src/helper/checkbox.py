import pygame as py


class CheckBox:
    def __init__(self, screen, default, size, checked, line_width=1, hover=None):
        self.screen = screen
        self.default = default
        self.size = size
        self.line_width = line_width
        self.is_checked = checked
        self.is_hovering = False
        self.rect = None
        if hover is None:
            self.hover = default
        else:
            self.hover = hover

    def render(self, mouse_position, x, y):
        self.rect = py.draw.rect(self.screen, self.default, [x, y, self.size, self.size], self.line_width)
        if self.is_checked:
            top = self.rect.top + (2 * self.line_width)
            bottom = self.rect.bottom - (2 * self.line_width)
            right = self.rect.right - (2 * self.line_width)
            left = self.rect.left + (2 * self.line_width)
            py.draw.line(self.screen, self.get_background(), [left, top], [right, bottom], self.line_width)
            py.draw.line(self.screen, self.get_background(), [left, bottom], [right, top], self.line_width)
        self.check_hover(mouse_position)

    def get_background(self):
        if self.is_hovering:
            return self.hover
        else:
            return self.default

    def check_hover(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            self.is_hovering = True
        else:
            self.is_hovering = False

    def is_clicked(self, mouse_position):
        return self.rect.collidepoint(mouse_position)
