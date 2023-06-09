
import random
import time

motiv_dict={
    # Bb_Bb
    "Bb_Bb": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Bb_Schema"
    },
    "Bb_Bb2": {
        "answer": "kurshaltepflichtig",
        "schema": "Bb_Bb_Schema2"
    },
    "Bb_Bb3": {
        "answer": "kurshaltepflichtig",
        "schema": "Bb_Bb_Schema2"
    },
    "Bb_Bb4": {
        "answer": "kurshaltepflichtig",
        "schema": "Bb_Bb_Schema2"
    },
    "Bb_Bb5": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Bb_Schema"
    },
    "Bb_Bb5": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Bb_Schema"
    },
    "Bb_Bb6": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Bb_Schema"
    },
    "Bb_Bb7": {
        "answer": "ausweichpflichtig",  # nein
        "schema": "Bb_Bb_Schema"  # nein
    },
    "Bb_Bb8": {
        "answer": "kurshaltepflichtig",
        "schema": "Bb_Bb_Schema2"
    },
    "Bb_Bb9": {
        "answer": "kurshaltepflichtig",
        "schema": "Bb_Bb_Schema2"
    },
    "Bb_Bb10": {
        "answer": "kurshaltepflichtig",
        "schema": "Bb_Bb_Schema2"
    },
    "Bb_Bb11": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Bb_Schema"
    },
    # Bb_Stb
    "Bb_Stb": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema"
    },
    "Bb_Stb2": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema2"
    },
    "Bb_Stb3": {
        "answer": ["ausweichpflichtig", "unklar"],
        "schema": "Bb_Stb_Schema"
    },
    "Bb_Stb4": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema"
    },
    "Bb_Stb5": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema"
    },
    "Bb_Stb6": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema"
    },
    "Bb_Stb6": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema"
    },
    "Bb_Stb7": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema"    # ggf. 3
    },
    "Bb_Stb8": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema"
    },
    "Bb_Stb9": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema2"
    },
    "Bb_Stb10": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema"
    },
    "Bb_Stb11": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema"
    },
    "Bb_Stb12": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema"
    },
    "Bb_Stb13": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema"   #3
    },

    # Stb_Bb
    "Stb_Bb": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema2"
    },
    "Stb_Bb2": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema"
    },
    "Stb_Bb3": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema2"
    },
    "Stb_Bb4": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema2"
    },
    "Stb_Bb5": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema2"
    },
    "Stb_Bb6": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema2"
    },
    "Stb_Bb7": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema"
    },
    "Stb_Bb8": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema2"
    },
    "Stb_Bb9": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema2"
    },
    "Stb_Bb10": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema2"
    },
    "Stb_Bb11": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema2"      #3
    },

    # Stb_Stb
    "Stb_Stb": {
        "answer": "ausweichpflichtig",
        "schema": "Stb_Stb_Schema"
    },
    "Stb_Stb2": {
        "answer": ["ausweichpflichtig", "unklar"],
        "schema": "Stb_Stb_Schema2"      #3
    },
    "Stb_Stb3": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Stb_Schema2"
    },
    "Stb_Stb4": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Stb_Schema2"
    },
    "Stb_Stb5": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Stb_Schema2"
    },
    "Stb_Stb6": {   # Bild falsch
        "answer": ["ausweichpflichtig", "unklar"],
        "schema": "Stb_Stb_Schema2"      #3
    },
    "Stb_Stb7": {
        "answer": "ausweichpflichtig",
        "schema": "Stb_Stb_Schema"
    },
    "Stb_Stb8": {
        "answer": "ausweichpflichtig",
        "schema": "Stb_Stb_Schema"
    },
    "Stb_Stb9": {
        "answer": ["ausweichpflichtig", "unklar"],
        "schema": "Stb_Stb_Schema2"    #3
    },
    "Stb_Stb10": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Stb_Schema2"
    },
    "Stb_Stb11": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Stb_Schema2"
    },
    "Stb_Stb12": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Stb_Schema2"
    },
    "Stb_Stb13": {
        "answer": "ausweichpflichtig",
        "schema": "Stb_Stb_Schema"
    },

}




class quiz_sailing():

    def __init__(self):

        questionlist = list(motiv_dict.keys())
        self.questionlist = questionlist

        self.sequenz = None
        self.counter_correct = 0
        self.counter_false = 0
        self.pic_question = None

    def start(self, number_questions = 10):
        # number_questions = 10

        selected_questions = []

        while len(selected_questions) < number_questions:

            element_add = random.choice(self.questionlist)

            if element_add not in selected_questions:
                selected_questions.append(element_add)

        self.sequenz = selected_questions
        self.counter_correct = 0
        self.counter_false = 0
        self.pic_question = selected_questions[0]

    def show_question(self):
        return self.pic_question

    def show_correct_count(self):
        return str(self.counter_correct)
    
    def show_false_count(self):
        return str(self.counter_false)

    def answer_question(self, answer):

        try:
            if answer == motiv_dict[self.pic_question]["answer"]:
                if len(self.sequenz) >1:
                    self.sequenz = self.sequenz[1:]
                    self.pic_question = self.sequenz[0]
                    self.counter_correct = self.counter_correct  + 1
                elif len(self.sequenz) == 1:
                    self.pic_question = "Stb_start"

            elif answer != motiv_dict[self.pic_question]["answer"]:
                self.pic_question = motiv_dict[self.pic_question]["schema"]
                self.counter_false = self.counter_false  + 1

            return self.pic_question 
        except KeyError:
            return self.continue_quiz()

    def continue_quiz(self):

        try:
            if "Schema" in self.pic_question:
                if len(self.sequenz) >1:
                    self.sequenz = self.sequenz[1:]
                    self.pic_question = self.sequenz[0]
                    # self.counter_false = self.counter_false  + 1
                elif self.sequenz == 1:
                    self.pic_question = "Stb_start"

            else:
                if len(self.sequenz) >1:
                    self.sequenz = self.sequenz[1:]
                    self.pic_question = self.sequenz[0]
                    # self.counter_false = self.counter_false  + 1
                elif self.sequenz == 1:
                    self.pic_question = "Stb_start"
        except TypeError:
            self.pic_question = "Stb_start"

        return self.pic_question


# kurshaltepflichtig    
# ausweichpflichtig
