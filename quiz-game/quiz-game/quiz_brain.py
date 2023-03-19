
class QuizBrain:
    def __init__(self,q_list):
        self.question_list = q_list
        self.question_number = 0
        self.current_score = 0
    def next_question(self):
        current_question =  self.question_list[self.question_number]
        self.question_number += 1
        user_type = input(f'Q.{self.question_number} : {current_question.text}(True/False)? ')
        self.check_answer(user_type,current_question.answer)

    def still_has_question(self):
        while self.question_number < len(self.question_list):
            self.next_question()
        else:
            print(f"Your total score is {self.current_score}/12")
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.current_score += 1
            print("You got it right")
        else:
            print("You are wrong")
        print(f'Your score is {self.current_score}/{self.question_number}')

