
import random
import time

# kurshaltepflichtig    
# ausweichpflichtig

motiv_dict={
    # Bb_Bb
    "Bb_Bb1": {
        "answer": "kurshaltepflichtig",
        "schema": "Bb_Bb_Schema"
    },
    "Bb_Bb2": {
        "answer": "kurshaltepflichtig",
        "schema": "Bb_Bb_Schema"
    },
    # Bb_Stb
    "Bb_Stb1": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema"
    },
    "Bb_Stb2": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema2"
    },
    "Bb_Stb3": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Stb_Schema3"
    },
    # Stb_Bb
    "Stb_Bb1": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema"
    },
    "Stb_Bb2": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema2"
    },
    "Stb_Bb3": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Bb_Schema3"
    },
    # Stb_Stb
    "Stb_Stb1": {
        "answer": "kurshaltepflichtig",
        "schema": "Stb_Stb_Schema"
    },
    "Stb_Stb2": {
        "answer": "ausweichpflichtig",
        "schema": "Bb_Bb_Schema"
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

    def show_question(self):
        return self.pic_question

    def show_correct_count(self):
        return str(self.counter_correct)
    
    def show_false_count(self):
        return str(self.counter_false)
    
    def show_jumper_count(self):
        return str(self.counter_jumper)

    def answer_question(self, answer):

        try:
            if answer == motiv_dict[self.pic_question]["answer"]:
                if len(self.sequenz) >1:
                    self.sequenz = self.sequenz[1:]
                    self.pic_question = self.sequenz[0]
                    self.counter_correct = self.counter_correct  + 1

                elif len(self.sequenz) == 1:
                    self.counter_correct = self.counter_correct  + 1
                    self.sequenz = ["Stb_start"]
                    self.pic_question = "Stb_start"

            elif answer != motiv_dict[self.pic_question]["answer"]:
                self.pic_question = motiv_dict[self.pic_question]["schema"]
                self.counter_false = self.counter_false  + 1

            return self.pic_question 

        except BaseException:
            return self.continue_quiz()

    def continue_quiz(self):

        try:
            if "Schema" in self.pic_question:
                if len(self.sequenz) >1:
                    self.sequenz = self.sequenz[1:]
                    self.pic_question = self.sequenz[0]

                else:
                    self.sequenz = ["Stb_start"]
                    self.pic_question = "Stb_start"

            else:
                if len(self.sequenz) >1:
                    self.counter_jumper = self.counter_jumper  + 1
                    self.sequenz = self.sequenz[1:]
                    self.pic_question = self.sequenz[0]

                else:
                    if self.counter_false + self.counter_correct + self.counter_jumper < self.number_questions:
                        self.counter_jumper = self.counter_jumper  + 1
                    self.sequenz = ["Stb_start"]
                    self.pic_question = "Stb_start"

        except BaseException:
            self.pic_question = "Stb_start"

        return self.pic_question


# kurshaltepflichtig    
# ausweichpflichtig
