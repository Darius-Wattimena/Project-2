import pygame as py

class Button:
    def __init__(self, screen, text, default, hover, font_color, font_color_hover, font_size):
        self.screen = screen
        self.text = text
        self.default = default
        self.hover = hover
        self.font_color = font_color
        self.font_color_hover = font_color_hover
        self.font_size = font_size
        self.is_hovering = False

    def get_background(self):
        if self.is_hovering:
            return self.hover
        else:
            return self.default

    def render_text(self):
        font = py.font.Font(None, self.font_size)
        if self.is_hovering:
            return font.render(self.text, True, self.font_color_hover)
        else:
            return font.render(self.text, True, self.font_color)

    def render(self, mouse_position, rect_coord):
        self.obj = py.draw.rect(self.screen, self.get_background(), rect_coord)
        text = self.render_text()
        text_rect = text.get_rect(center = self.obj.center)
        self.screen.blit(text, text_rect)
        self.check_hover(mouse_position)

    def check_hover(self, mouse_position):
        if self.obj.collidepoint(mouse_position):
            self.is_hovering = True
        else:
            self.is_hovering = False
