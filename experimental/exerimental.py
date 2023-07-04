

from backup_kivy.quiz import (quiz_sailing)

from sail_rightofway.quiz import (quiz_sailing)

from sail_rightofway.quiz import (motiv_dict)


# kurshaltepflichtig
# ausweichpflichtig


my_quiz = quiz_sailing()

my_quiz.start()
my_quiz.start(number_questions=10)
my_quiz.start(number_questions=3, questionmodus="situation")

# TODO: hier weiter testen und dran arbeiten
my_quiz.start(number_questions=10, questionmodus="schema")

my_quiz.sequenz
# ['Bb_Stb3', 'Bb_Bb1', 'Bb_Bb2', 'Stb_Bb3', 'Stb_Bb2', 'Stb_Bb1', 'Bb_Stb2', 'Stb_Stb2', 'Bb_Stb1', 'Stb_Stb1']
motiv_dict[my_quiz.sequenz[0]]["question_schema"]
motiv_dict[my_quiz.sequenz[0]]["answer"]

# my_quiz.pic_question == motiv_dict[my_quiz.sequenz[0]]["question_schema"]


my_quiz.show_question()
my_quiz.show_answer()

my_quiz.show_correct_count()


my_quiz.answer_question(answer="kurshaltepflichtig")

my_quiz.answer_question(answer="ausweichpflichtig")

my_quiz.continue_quiz()



# Stb_Bb_Frage2, Bb_Bb_Frage1, Bb_Stb_Frage2, Bb_Bb_Frage2


my_quiz.show_question()

my_quiz.show_answer()

my_quiz.show_correct_count()
my_quiz.show_false_count()
my_quiz.show_jumper_count()

"Schema" in my_quiz.show_question()

my_quiz.sequenz
my_quiz.questionlist

