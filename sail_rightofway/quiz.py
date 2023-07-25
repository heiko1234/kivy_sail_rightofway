
import random
import time

# kurshaltepflichtig    
# ausweichpflichtig


# TODO: umbau auf "key" with "question"

motiv_dict={
    # Bb_Bb
    "Bb_Bb1": {
        "question_situation": "Bb_Bb1",
        "question_schema": "Bb_Bb_Frage1",
        "answer": "kurshaltepflichtig",
        "schema": "Bb_Bb_Schema",
        "wind": "wind_315"
    },
    "Bb_Bb2": {
        "question_situation": "Bb_Bb2",
        "question_schema": "Bb_Bb_Frage2",
        "answer": "kurshaltepflichtig",
        "schema": "Bb_Bb_Schema",
        "wind": "wind_315"
    },
    # Bb_Stb
    "Bb_Stb1": {
        "question_situation": "Bb_Stb1",
        "question_schema": "Bb_Stb_Frage1",
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema",
        "wind": "wind_270"
    },
    "Bb_Stb2": {
        "question_situation": "Bb_Stb2",
        "question_schema": "Bb_Stb_Frage2",
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema2",
        "wind": "wind_225"
    },
    "Bb_Stb3": {
        "question_situation": "Bb_Stb3",
        "question_schema": "Bb_Stb_Frage3",
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema3",
        "wind": "wind_315"
    },
    # Stb_Bb
    "Stb_Bb1": {
        "question_situation": "Stb_Bb1",
        "question_schema": "Stb_Bb_Frage1",
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema",
        "wind": "wind_90"
    },
    "Stb_Bb2": {
        "question_situation": "Stb_Bb2",
        "question_schema": "Stb_Bb_Frage2",
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema2",
        "wind": "wind_135"
    },
    "Stb_Bb3": {
        "question_situation": "Stb_Bb3",
        "question_schema": "Stb_Bb_Frage3",
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema3",
        "wind": "wind_45"
    },
    # Stb_Stb
    "Stb_Stb1": {
        "question_situation": "Stb_Stb1",
        "question_schema": "Stb_Stb_Frage1",
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Stb_Schema",
        "wind": "wind_45"
    },
    "Stb_Stb2": {
        "question_situation": "Stb_Stb2",
        "question_schema": "Stb_Stb_Frage2",
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
        self.true_false_answer = True
        self.wind = "wind_00"
        self.questionmodus = "situation"   #schema
        self.situation = None

    def start(self, number_questions = 10, questionmodus="situation"):

        self.number_questions = number_questions
        # number_questions = 10

        selected_questions = []

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
        self.situation = selected_questions[0]
        self.true_false_answer = True
        self.wind = motiv_dict[self.situation]["wind"]
        self.questionmodus = questionmodus
        self.pic_question = None

    def show_questionmodus(self):
        return str(self.questionmodus)

    def show_question(self):
        # TODO: hier ist irgentwo der fehler, aber nur bei schema
        # if self.questionmodus == "schema"
        # if self.questionmodus == "situation"

        # if len(self.sequenz) == 1:

        if self.sequenz == None:
            return "Stb_start"

        if (self.sequenz != ["Stb_start"]) and (len(self.sequenz) >= 1) and (self.true_false_answer == True):
            if self.questionmodus == "situation":
                return motiv_dict[self.situation]["question_situation"]
            elif self.questionmodus == "schema":
                return motiv_dict[self.situation]["question_schema"]

        elif (self.sequenz != ["Stb_start"]) and (len(self.sequenz) >= 1) and (self.true_false_answer == False):
            return motiv_dict[self.situation]["schema"]


        elif (len(self.sequenz)==1) and (self.sequenz == ["Stb_start"]):
            return "Stb_start"

        else:
            return "Stb_start"

    def show_answer(self):
        try:
            return motiv_dict[self.situation]["answer"]
        except BaseException:
            print("No Answer")

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

        true_false_mode  = self.true_false_answer

        try:
            if (answer == motiv_dict[self.sequenz[0]]["answer"]) and (true_false_mode == True):

                print("answer is correct")

                self.true_false_answer = True

                if len(self.sequenz) == 1:
                    self.counter_correct = self.counter_correct  + 1
                    self.sequenz = ["Stb_start"]
                    self.situation = self.sequenz[0]
                    self.pic_question = "Stb_start"
                    self.wind = "wind_00"


                elif len(self.sequenz) >1:
                    self.sequenz = self.sequenz[1:]
                    self.situation = self.sequenz[0]
                    self.counter_correct = self.counter_correct  + 1
                    self.wind = motiv_dict[self.situation]["wind"]

                    if self.questionmodus == "situation":
                        self.pic_question = motiv_dict[self.situation]["question_situation"]
                    elif self.questionmodus == "schema":
                        self.pic_question = motiv_dict[self.situation]["question_schema"]



            elif (answer != motiv_dict[self.situation]["answer"]) and (true_false_mode == True):

                print("answer is false")

                self.true_false_answer = False
                self.counter_false = self.counter_false + 1

                self.pic_question = motiv_dict[self.situation]["schema"]

            elif true_false_mode == False:
                return self.continue_quiz()

            return self.pic_question

        except BaseException as be:
            print(f"exception on answering questions: {be}")


    def continue_quiz(self):
        # if self.questionmodus == "schema"
        # if self.questionmodus == "situation"

        if self.sequenz == None:
            return "Stb_start"

        true_false_mode  = self.true_false_answer

        if (len(self.sequenz) >= 1) and self.sequenz != ["Stb_start"]:

            if true_false_mode == True:
                self.counter_jumper = self.counter_jumper  + 1

            try:
                self.sequenz = self.sequenz[1:]
                self.situation = self.sequenz[0]
                self.wind = motiv_dict[self.situation]["wind"]

                if self.questionmodus == "situation":
                    self.pic_question = motiv_dict[self.situation]["question_situation"]
                elif self.questionmodus == "schema":
                    self.pic_question = motiv_dict[self.situation]["question_schema"]

                if self.true_false_answer == False:
                    self.true_false_answer = True

            except BaseException:
                self.sequenz = ["Stb_start"]
                self.pic_question = "Stb_start"
                self.situation = self.sequenz[0]
                self.wind = "wind_00"



        # elif len(self.sequenz) == 1:
        else:
            self.sequenz = ["Stb_start"]
            self.pic_question = "Stb_start"
            self.situation = self.sequenz[0]
            self.wind = "wind_00"


# kurshaltepflichtig
# ausweichpflichtig
