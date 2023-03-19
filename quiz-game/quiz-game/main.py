from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
   question_text = question['text']
   question_answer = question['answer']
   question_bank.append(Question(question_text,question_answer))

quiz_brain = QuizBrain(question_bank)
quiz_brain.still_has_question()