from data import questions
from question_model import Questions
from quiz_brain import QuizBrain

questions_bank = []

for question in questions:
    questions_bank.append(Questions(question["text"], question["answer"]))


quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Thanks! \nYou have completed the Quiz!")
print(f"Your Final Score: {quiz.score}/{len(quiz.questions_bank)}")
if quiz.score >= (len(quiz.questions_bank)/2):
    print("Congratulations! Passed!")
else:
    print("Failed!")
