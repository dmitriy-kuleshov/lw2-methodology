import random
from src.cli import attempt_quiz


def progression_question():
    start_point = random.randint(1, 9)
    mystery_point = random.randint(0, 5)
    sequence = [start_point * (start_point ** i) for i in range(6)]
    answer = sequence[mystery_point]
    formatted_question = ' '.join(map(str, sequence)).replace(str(answer), "..", 1)
    return {'sequence': sequence, 'answer': answer, 'formatted_question': formatted_question}


def progression_answer(question_data):
    return question_data['answer']


def progression(username):
    attempt_quiz(username, progression_question, progression_answer)
