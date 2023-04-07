

from sail_rightofway.quiz import (quiz_sailing)


# kurshaltepflichtig    
# ausweichpflichtig


my_quiz = quiz_sailing()

my_quiz.start()
my_quiz.start(number_questions=10)

my_quiz.show_question()

my_quiz.show_correct_count()




my_quiz.answer_question(answer="kurshaltepflichtig")

my_quiz.answer_question(answer="ausweichpflichtig")

my_quiz.continue_quiz()



my_quiz.show_question()

my_quiz.show_correct_count()

"Schema" in my_quiz.show_question()

my_quiz.sequenz

