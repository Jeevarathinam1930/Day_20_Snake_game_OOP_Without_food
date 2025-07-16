class Quiz_brain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def still_has_question(self):
        length=len(self.question_list)
        if self.question_number<length:
            return True
        else:
            return False
    def asking_question(self):
        question_text=self.question_list[self.question_number]
        self.question_number+=1
        user_anser=input(f"Q.{self.question_number}: {question_text.question} (True/False)?:")
        self.check_answer(user_anser,question_text.answer)
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You got it right")
            self.score+=1
            print(f"You current score is:{self.score}/{self.question_number}")
        else:
            print("That's wrong")
            print(f"You current score is:{self.score}/{self.question_number}")
        print(f"The correct answer is {correct_answer}!")