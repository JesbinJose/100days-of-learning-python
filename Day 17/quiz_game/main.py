from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import os
import random


question_bank = []

for question in question_data:
    new_question = Question(question)
    question_bank.append(new_question)
random.shuffle(question_bank)
quiz  = QuizBrain(question_bank)

os.system('cls')

while quiz.still_has_questions():
    quiz.next_question()

quiz.finsh_game()