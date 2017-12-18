import pygame as py

class Button:
    def __init__(self, screen, text, default, hover, font_color, font_color_hover, font_size, width, height):
        self.screen = screen
        self.text = text
        self.default = default
        self.hover = hover
        self.font_color = font_color
        self.font_color_hover = font_color_hover
        self.font_size = font_size
        self.is_hovering = False
        self.width = width
        self.height = height
        self.rect = None

    def get_background(self):
        if self.is_hovering:
            return self.hover
        else:
            return self.default

    def render_text(self):
        font = py.font.Font("resources/fonts/Carnevalee Freakshow.ttf", self.font_size)
        if self.is_hovering:
            return font.render(self.text, True, self.font_color_hover)
        else:
            return font.render(self.text, True, self.font_color)

    def render(self, mouse_position, x, y, border=0):
        self.rect = py.draw.rect(self.screen, self.get_background(), [x, y, self.width, self.height], border)
        text = self.render_text()
        text_rect = text.get_rect(center=self.rect.center)
        self.screen.blit(text, text_rect)
        self.check_hover(mouse_position)

    def check_hover(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            self.is_hovering = True
        else:
            self.is_hovering = False

    def is_clicked(self, mouse_position):
        if self.rect != None:
            return self.rect.collidepoint(mouse_position)
