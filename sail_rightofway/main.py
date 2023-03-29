


# https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py
# Kivy MD
# https://www.youtube.com/watch?v=LRXo0juuTrw&list=PLhTjy8cBISEoQQLZ9IBlVlr4WjVoStmy-

# from kivy.config import Config
# Config.set('kivy','keyboard_mode','systemanddock')


from kivymd.app import MDApp

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast.kivytoast.kivytoast import toast

# from sail_class import sail_infos, sail_scenario


# Properties
from kivy.properties import ObjectProperty

# Clock
from kivy.clock import Clock

# background Threading
from threading import Thread

# partial: funktions reverenz + parameter übergabe
from functools import partial


# Define our differeent screens
class WelcomeWindow(Screen):

    # def on_enter(self, *args):
    #     # on_enter works automatically, while keyword
    #     Clock.schedule_once(self.switch_to_second_view, 3)

    def entrance_button_behavior(self, *args):
        Clock.schedule_once(self.switch_to_second_view, 1)

    def switch_to_second_view(self, *args):
        self.manager.current = "quizwindow"
        self.manager.transition.direction="left"


# init the boat outside of Screen
# boat_questions = quiz()


class QuizWindow(Screen):

    # pictures
    sail_png = ObjectProperty(None)

    def any_function():
        pass










# https://github.com/kivymd/KivyMD/wiki/Modules-Material-App#exceptions
class SailApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Sail Right of Way App"
        super().__init__(**kwargs)

    def build(self):
        # Load file function musst be in build and not before
        kv = Builder.load_file("Sail_rightofway.kv")
        self.root = kv


if __name__ == "__main__":
    SailApp().run()

