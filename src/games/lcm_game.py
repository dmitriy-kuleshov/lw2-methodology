import math
import random
from src.cli import attempt_quiz


def lcm_question():
    numbers = random.sample(range(1, 500), 3)
    formatted_question = ' '.join(map(str, numbers))
    return {'numbers': numbers, 'formatted_question': formatted_question}


def lcm_answer(question_data):
    numbers = question_data['numbers']
    lcm = numbers[0]
    for element in numbers[1:]:
        lcm = lcm * element // math.gcd(lcm, element)
    return lcm


def lcm_alg(username):
    attempt_quiz(username, lcm_question, lcm_answer)
