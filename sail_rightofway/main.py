

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

from kivy.storage.jsonstore import JsonStore



# init the boat outside of Screen
from quiz import quiz_sailing

boat_questions = quiz_sailing()



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

        # boat_questions.start(number_questions = 10)





class SetupWindow(Screen):

    number_of_questions = ObjectProperty()

    def any_function(self, *args):
        pass

    def switch_to_second_view(self, *args):
        self.manager.current = "quizwindow"
        self.manager.transition.direction="right"

    def restart_quiz(self, *args):

        try:
            question_number = int(self.number_of_questions.text)
            if question_number >= 30:
                question_number = 30
            elif (question_number <= 30) and (question_number >= 10):
                question_number = question_number

            elif question_number < 4:
                question_number = 4

        except BaseException:
            question_number = 10

        # store = JsonStore("sail_rightofway/numberofquestions.json")
        store = JsonStore("numberofquestions.json")

        store.put("question_number", question_number=question_number)

        boat_questions.start(number_questions = question_number)



class QuizWindow(Screen):

    # pictures
    sail_png = ObjectProperty(None)
    false_counter = ObjectProperty(None)
    true_counter = ObjectProperty(None)
    jumper_counter = ObjectProperty(None)

    def switch_to_setup_view(self, *args):
        self.manager.current = "setupwindow"
        self.manager.transition.direction="left"

    def any_function(self, *args):
        pass

    def restart_quiz(self, *args):

        # store = JsonStore("sail_rightofway/numberofquestions.json")
        store = JsonStore("numberofquestions.json")

        try:
            store.get("question_number")
            question_number = store.get("question_number")["question_number"]
        except BaseException:
            question_number = 10


        boat_questions.start(number_questions = question_number)

        self.show_png()

        self.false_counter.text = str(0)
        self.true_counter.text = str(0)
        self.jumper_counter.text = str(0)

    def show_png(self, *args):
        output = boat_questions.show_question()
        try:
            if "Schema" not in output:
                self.sail_png.source = f"assets/sails/{output}.png"
            else:
                self.sail_png.source = f"assets/schema/{output}.png"
        except TypeError:
            pass


    def ausweichen(self, *args):
        boat_questions.answer_question(answer = "ausweichpflichtig")
        self.show_png()

        self.false_counter.text = boat_questions.show_false_count()
        self.true_counter.text = boat_questions.show_correct_count()
        self.jumper_counter.text = boat_questions.show_jumper_count()

    def kurshalten(self, *args):
        boat_questions.answer_question(answer = "kurshaltepflichtig")
        self.show_png()

        self.false_counter.text = boat_questions.show_false_count()
        self.true_counter.text = boat_questions.show_correct_count()
        self.jumper_counter.text = boat_questions.show_jumper_count()

    def weiter(self, *args):
        boat_questions.continue_quiz()
        self.show_png()

        self.false_counter.text = boat_questions.show_false_count()
        self.true_counter.text = boat_questions.show_correct_count()
        self.jumper_counter.text = boat_questions.show_jumper_count()








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



