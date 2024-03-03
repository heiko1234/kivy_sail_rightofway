# https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py
# Kivy MD
# https://www.youtube.com/watch?v=LRXo0juuTrw&list=PLhTjy8cBISEoQQLZ9IBlVlr4WjVoStmy-
# from kivy.config import Config
# Config.set('kivy','keyboard_mode','systemanddock')
#
#
# Kivy MD
# init the boat outside of Screen
from quiz import quiz_sailing

from kivymd.app import MDApp

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
# from kivymd.toast.kivytoast.kivytoast import toast
from kivymd.toast import toast

from kivy.core.audio import SoundLoader

# from sail_class import sail_infos, sail_scenario


# Properties
from kivy.properties import ObjectProperty

# Clock
from kivy.clock import Clock

# background Threading
# from threading import Thread

# partial: funktions reverenz + parameter übergabe
# from functools import partial

from kivy.storage.jsonstore import JsonStore

# Open a weblink
import webbrowser



boat_questions = quiz_sailing()



from kivymd.uix.label import MDLabel
# from kivy.uix.togglebutton import ToggleButton



# from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
# from kivymd.uix.button import MDFlatButton


# class MyToggleButton(MDFlatButton, MDToggleButton):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.background_down = "lightgreen"


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


class LawWindow(Screen):

    def any_functin(self, *args):
        pass

    def entrance_button_behavior(self, *args):
        Clock.schedule_once(self.switch_to_second_view, 1)

    def switch_to_second_view(self, *args):
        self.manager.current = "quizwindow"
        self.manager.transition.direction="right"


class Haftungindow(Screen):

    def any_functin(self, *args):
        pass

    def entrance_button_behavior(self, *args):
        Clock.schedule_once(self.switch_to_second_view, 1)

    def switch_to_second_view(self, *args):
        self.manager.current = "quizwindow"
        self.manager.transition.direction="left"

    def hyperlink_open(self, *args):
        webbrowser.open("https://github.com/heiko1234/kivy_sail_rightofway/blob/main/Datenschutzbestimmung.md")


class AnleitungWindow(Screen):

    def any_functin(self, *args):
        pass

    def entrance_button_behavior(self, *args):
        Clock.schedule_once(self.switch_to_second_view, 1)

    def switch_to_second_view(self, *args):
        self.manager.current = "quizwindow"
        self.manager.transition.direction="left"



class ConfigurationWindow(Screen):

    number_of_questions = ObjectProperty()
    # TODO
    questionmode = ObjectProperty()
    questionmode_alternative = ObjectProperty()
    # questionmode_text = ObjectProperty()

    def any_function(self, *args):
        pass

    def on_enter(self, *args):

        store = JsonStore("numberofquestions.json")
        try:
            questionmodus = store.get("questionmode")["questionmode"]
        except BaseException:
            questionmodus= "schema"
            store.put("questionmode", questionmode=questionmodus)


        # TODO
        # if questionmodus == "situation":
        #     self.questionmode.state = "down"
        # elif questionmodus == "schema":
        #     self.questionmode_alternative.state = "down"
        # else:
        #     self.questionmode.state = "down"

        if questionmodus == "situation":
            #self.questionmode_text.text = "situativ"
            self.questionmode.text_color= "white"
            self.questionmode.md_bg_color= "blue"
            self.questionmode_alternative.md_bg_color= "white"
            self.questionmode_alternative.text_color= "blue"
            # pass
        elif questionmodus == "schema":
            #self.questionmode_text.text = "schematisch"
            self.questionmode.text_color= "blue"
            self.questionmode.md_bg_color= "white"
            self.questionmode_alternative.md_bg_color= "blue"
            self.questionmode_alternative.text_color= "white"
            # pass
        else:
            pass



    def switch_to_second_view(self, *args):
        self.manager.current = "quizwindow"
        self.manager.transition.direction="right"


    # TODO: make this funktion work with the modus. need to create on quiz
    def questionmodus(self, *args, **kwargs):
        # print(f"args question: {args}")
        # print(f"kargs question: {kwargs}")

        store = JsonStore("numberofquestions.json")

        # print(f"questionmode: {self.questionmode.state}")

        # TODO
        # if self.questionmode.state == "down":
        #     questionmode = "situation"
        # else:
        #     questionmode = "schema"

        questionmode = "situation"

        store.put("questionmode", questionmode=questionmode)

        # self.questionmode_text.text = questionmode
        self.questionmode.text_color= "white"
        self.questionmode.md_bg_color= "blue"
        self.questionmode_alternative.md_bg_color= "white"
        self.questionmode_alternative.text_color= "blue"

    def questionmodus_alternative(self, *args, **kwargs):
        # print(f"args question: {args}")
        # print(f"kargs question: {kwargs}")

        store = JsonStore("numberofquestions.json")

        # print(f"questionmode: {self.questionmode.state}")

        # TODO
        # if self.questionmode.state == "down":
        #     questionmode = "situation"
        # else:
        #     questionmode = "schema"

        questionmode = "schema"

        store.put("questionmode", questionmode=questionmode)

        # self.questionmode_text.text = questionmode
        self.questionmode.text_color= "blue"
        self.questionmode.md_bg_color= "white"
        self.questionmode_alternative.md_bg_color= "blue"
        self.questionmode_alternative.text_color= "white"

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

        question_mode = store.get("questionmode")["questionmode"]
        print(f"question_mode: {question_mode}")


        boat_questions.start(number_questions = question_number, questionmodus=question_mode)



class QuizWindow(Screen):

    # pictures
    sail_png = ObjectProperty(None)
    false_counter = ObjectProperty(None)
    true_counter = ObjectProperty(None)
    jumper_counter = ObjectProperty(None)
    wind_png = ObjectProperty(None)

    def switch_to_setup_view(self, *args):
        self.manager.current = "configurationwindow" # "setupwindow"
        self.manager.transition.direction="left"

    def any_function(self, *args):
        pass

    def hyperlink_issues_open(self, *args):
        webbrowser.open("https://github.com/heiko1234/kivy_sail_rightofway/issues")

    def play_crashsound(self, *args):
        sound = SoundLoader.load("assets/sounds/boat_hit.wav")
        if sound:
            sound.play()

    def play_successsound(self, *args):
        sound = SoundLoader.load("assets/sounds/success3.wav")
        if sound:
            sound.play()

    def play_sound(self, *args):
        output = boat_questions.show_true_false_answer()

        if output is None:
            pass
        elif output:
            self.play_successsound()
        else:
            self.play_crashsound()



    def switch_to_lawview(self, *args):
        self.manager.current = "lawwindow"
        self.manager.transition.direction="left"

    def switch_to_haftungsview(self, *args):
        self.manager.current = "haftungwindow"
        self.manager.transition.direction="right"

    def switch_to_anleitungview(self, *args):
        self.manager.current = "anleitungwindow"
        self.manager.transition.direction="right"


    def restart_quiz(self, *args):

        # store = JsonStore("sail_rightofway/numberofquestions.json")
        store = JsonStore("numberofquestions.json")

        try:
            # store.get("question_number")
            question_number = store.get("question_number")["question_number"]
        except BaseException:
            question_number = 10

        try:
            question_mode = store.get("questionmode")["questionmode"]

        except BaseException:
            question_mode = "situation"

        print(f"question_mode: {question_mode}")


        boat_questions.start(number_questions = question_number, questionmodus=question_mode)

        self.show_png()
        self.show_wind_png()

        self.false_counter.text = str(0)
        self.true_counter.text = str(0)
        self.jumper_counter.text = str(0)

    def show_png(self, *args):
        output = boat_questions.show_question()
        questionmodus = boat_questions.show_questionmodus()

        true_false_answer_modus = boat_questions.true_false_answer

        # if questionmodus == "schema"
        # if questionmodus == "sitution"
        print(f"show_png main: {output}")
        try:
            if (true_false_answer_modus == True) and (questionmodus=="situation"):
                self.sail_png.source = f"assets/sails/{output}.png"
            elif (true_false_answer_modus == True) and (questionmodus=="schema"):
                self.sail_png.source = f"assets/question_schema/{output}.png"
            elif "Stb_start" == output:
                self.sail_png.source = f"assets/sails/{output}.png"
            elif true_false_answer_modus == False:
                self.sail_png.source = f"assets/schema/{output}.png"
            # else:
            #     self.sail_png.source = f"assets/schema/{output}.png"
        except TypeError:
            pass

    def show_wind_png(self, *args):
        output = boat_questions.show_wind()
        try:
            self.wind_png.source = f"assets/wind/{output}.png"
        except TypeError:
            pass

    def show_toaster(self, *args):
        output = boat_questions.show_true_false_answer()

        if output is None:
            pass

        elif output:
            toast(text="Antwort ist korrekt", duration=1.5)

        else:
            toast(text="Antwort ist falsch", duration=1.5)




    def ausweichen(self, *args):
        boat_questions.answer_question(answer = "ausweichpflichtig")
        self.show_png()
        self.show_wind_png()
        self.show_toaster()
        self.play_sound()

        self.false_counter.text = boat_questions.show_false_count()
        self.true_counter.text = boat_questions.show_correct_count()
        self.jumper_counter.text = boat_questions.show_jumper_count()

    def kurshalten(self, *args):
        boat_questions.answer_question(answer = "kurshaltepflichtig")
        self.show_png()
        self.show_wind_png()
        self.show_toaster()
        self.play_sound()

        self.false_counter.text = boat_questions.show_false_count()
        self.true_counter.text = boat_questions.show_correct_count()
        self.jumper_counter.text = boat_questions.show_jumper_count()

    def weiter(self, *args):
        boat_questions.continue_quiz()
        self.show_png()
        self.show_wind_png()
        # self.play_sound()
        self.play_successsound()

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



