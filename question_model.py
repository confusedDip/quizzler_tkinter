"""
question_model.py: A class defining the structure of a question
"""


class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
