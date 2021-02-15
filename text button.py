from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


class Option(Button):
    def __init__(self):
        super().__init__(
            model='circle',
            color=color.blue,
            scale=0.3)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                popup_text = Text("Hello, Im gay!")
                destroy(popup_text, delay=2)


demo_button = Option()

app.run()
