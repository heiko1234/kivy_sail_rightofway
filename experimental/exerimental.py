

from backup_kivy.quiz import (quiz_sailing)

from sail_rightofway.quiz import (quiz_sailing)


# kurshaltepflichtig
# ausweichpflichtig


my_quiz = quiz_sailing()

my_quiz.start()
my_quiz.start(number_questions=10)
my_quiz.start(number_questions=5, questionmodus="situation")
my_quiz.start(number_questions=10, questionmodus="schema")

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

