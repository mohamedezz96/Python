class QuizBrain:
    def __init__(self,questions_bank):
        self.question_number = 0 
        self.questions_bank = questions_bank
        self.score = 0 

    def still_has_questions(self):
        if (self.question_number < len(self.questions_bank)):
            return True
        else:
            return False
    
    def next_question(self):
        user_answer = input(f"Q{self.question_number + 1}. {self.questions_bank[self.question_number].text} (True/False): ").title()
        self.check_answer(user_answer, self.questions_bank[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("Correct!")
        else:
            print("Wrong!")

        print(f"You Current Score: {self.score}/{self.question_number + 1} ")
        print("\n")
