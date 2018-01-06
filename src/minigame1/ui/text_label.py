from src.helper.label import Label


class TextLabel(Label):
    def __init__(self, screen, text):
        super().__init__(screen, text, [255, 255, 255], 20, sys_font="calibri")
