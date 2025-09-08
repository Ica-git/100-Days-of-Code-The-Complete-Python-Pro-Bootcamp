from question_model import Question
from data import question_data
from quiz_brain import QuziBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(question_text, answer)
    question_bank.append(new_question)

quiz = QuziBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your score was: {quiz.score}/{len(question_bank)}.")
