
import random
import time

# kurshaltepflichtig    
# ausweichpflichtig


# TODO: umbau auf "key" with "question"

motiv_dict={
    # Bb_Bb
    "Bb_Bb1": {
        "question": "Bb_Bb1",
        "answer": "kurshaltepflichtig",
        "schema": "Bb_Bb_Schema",
        "wind": "wind_315"
    },
    "Bb_Bb2": {
        "question": "Bb_Bb2",
        "answer": "kurshaltepflichtig",
        "schema": "Bb_Bb_Schema",
        "wind": "wind_315"
    },
    # Bb_Stb
    "Bb_Stb1": {
        "question": "Bb_Stb1",
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema",
        "wind": "wind_270"
    },
    "Bb_Stb2": {
        "question": "Bb_Stb2",
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema2",
        "wind": "wind_225"
    },
    "Bb_Stb3": {
        "question": "Bb_Stb3",
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema3",
        "wind": "wind_315"
    },
    # Stb_Bb
    "Stb_Bb1": {
        "question": "Stb_Bb1",
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema",
        "wind": "wind_90"
    },
    "Stb_Bb2": {
        "question": "Stb_Bb2",
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema2",
        "wind": "wind_135"
    },
    "Stb_Bb3": {
        "question": "Stb_Bb3",
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema3",
        "wind": "wind_45"
    },
    # Stb_Stb
    "Stb_Stb1": {
        "question": "Stb_Stb1",
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Stb_Schema",
        "wind": "wind_45"
    },
    "Stb_Stb2": {
        "question": "Stb_Stb2",
        "answer": "ausweichpflichtig",
        "schema": "Bb_Bb_Schema",
        "wind": "wind_315"
    },
}


class quiz_sailing():

    def __init__(self):

        questionlist = list(motiv_dict.keys())
        self.questionlist = questionlist

        self.sequenz = None
        self.counter_correct = 0
        self.counter_false = 0
        self.counter_jumper = 0
        self.number_questions = 10
        self.pic_question = None
        self.true_false_answer = None
        self.wind = "wind_00"

    def start(self, number_questions = 10):

        self.number_questions = number_questions
        # number_questions = 10

        selected_questions = []

        number_questions = number_questions+0

        if number_questions <= len(self.questionlist):

            while len(selected_questions) < number_questions:

                element_add = random.choice(self.questionlist)

                if element_add not in selected_questions:
                    selected_questions.append(element_add)

        elif number_questions > len(self.questionlist):

            while len(selected_questions) < number_questions:

                element_add = random.choice(self.questionlist)

                selected_questions.append(element_add)


        self.sequenz = selected_questions
        self.counter_correct = 0
        self.counter_false = 0
        self.counter_jumper = 0
        self.pic_question = selected_questions[0]
        self.true_false_answer = None
        self.wind = motiv_dict[self.pic_question]["wind"]

    def show_question(self):
        if not "Schema" in self.pic_question:
            return motiv_dict[self.pic_question]["question"]
        else:
            return self.pic_question

    def show_correct_count(self):
        return str(self.counter_correct)

    def show_false_count(self):
        return str(self.counter_false)

    def show_jumper_count(self):
        return str(self.counter_jumper)

    def show_true_false_answer(self):
        return self.true_false_answer

    def show_wind(self):
        return str(self.wind)

    def answer_question(self, answer):

        try:
            if answer == motiv_dict[self.pic_question]["answer"]:

                self.true_false_answer = True

                if len(self.sequenz) >1:
                    self.sequenz = self.sequenz[1:]
                    # self.pic_question = self.sequenz[0]
                    self.pic_question = self.sequenz[0]["question"]
                    self.counter_correct = self.counter_correct  + 1
                    self.wind = motiv_dict[self.pic_question]["wind"]

                elif len(self.sequenz) == 1:
                    self.counter_correct = self.counter_correct  + 1
                    self.sequenz = ["Stb_start"]
                    self.pic_question = "Stb_start"
                    self.wind = "wind_00"

            elif answer != motiv_dict[self.pic_question]["answer"]:

                self.true_false_answer = False

                self.pic_question = motiv_dict[self.pic_question]["schema"]
                self.counter_false = self.counter_false  + 1
                # self.wind = motiv_dict[self.pic_question]["wind"]

            return self.pic_question

        except BaseException:
            return self.continue_quiz()

    def continue_quiz(self):

        try:
            if "Schema" in self.pic_question:
                if len(self.sequenz) >1:
                    self.sequenz = self.sequenz[1:]
                    self.pic_question = self.sequenz[0]
                    self.wind = motiv_dict[self.pic_question]["wind"]

                else:
                    self.sequenz = ["Stb_start"]
                    self.pic_question = "Stb_start"
                    self.wind = "wind_00"

            else:
                if len(self.sequenz) >1:
                    self.counter_jumper = self.counter_jumper  + 1
                    self.sequenz = self.sequenz[1:]
                    self.pic_question = self.sequenz[0]
                    # self.pic_question = self.sequenz[0]["question"]
                    self.wind = motiv_dict[self.pic_question]["wind"]

                else:
                    if self.counter_false + self.counter_correct + self.counter_jumper < self.number_questions:
                        self.counter_jumper = self.counter_jumper  + 1
                    self.sequenz = ["Stb_start"]
                    self.pic_question = "Stb_start"
                    self.wind = "wind_00"

        except BaseException:
            self.pic_question = "Stb_start"
            self.wind = "wind_00"

        return self.pic_question


# kurshaltepflichtig
# ausweichpflichtig
