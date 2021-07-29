from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank =[]
for ques in question_data:
    qt= ques["text"]
    qa= ques["answer"]
    new_question=Question(qt,qa)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
while quiz.still_has_question() :
    quiz.new_question()











