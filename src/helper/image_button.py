from src.helper.button import Button
import pygame as py


class ImageButton(Button):
    def __init__(self, screen, image_location, text, font_color, font_color_hover, font_size, width, height):
        self.image = py.image.load(image_location).convert_alpha()
        self.image = py.transform.scale(self.image, (width, height))
        super().__init__(screen, text, None, None, font_color, font_color_hover, font_size, width, height)

    def render(self, mouse_position, x, y, border=0):
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen.blit(self.image, self.rect)
        text = self.render_text()
        text_rect = text.get_rect(center=self.rect.center)
        self.screen.blit(text, text_rect)
        self.check_hover(mouse_position)
