class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0
    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        text = self.question_list[self.question_number]
        self.question_number +=1
        user = input(f"Q. {self.question_number} {text.question}  (True or False) ?")
        self.check_answer(user, text.answer)

    def check_answer(self, useranswer, correctanswer):
        if useranswer.lower() == correctanswer.lower():
            self.score += 1
            print(f"your answer is right and score = {self.score}")
        else:
            print("you got it wrong")
        print(f"correct answer is {correctanswer}")
