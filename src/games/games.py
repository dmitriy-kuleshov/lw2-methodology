import math
import random


def lcm_alg(username):
    print("Find the smallest common multiple of given numbers.")
    attempts = 0
    while attempts < 3:
        numbers = random.sample(range(0, 500), 3)
        output_numbers = ' '.join(map(str, numbers))
        print(f"Question: {output_numbers}")
        assumption = int(input("Your answer: "))

        lcm = numbers[0]
        for element in numbers[1:]:
            lcm = lcm * element // math.gcd(lcm, element)
        if lcm == assumption:
            print(f"Correct!\nCongratulation, {username}")
            break
        else:
            print(f"'{assumption}' is wrong answer;(.Correct answer was '{lcm}'.\n Let's try again, {username}!")
            attempts += 1


def progression(username):
    print("What number is missing in the progression?")
    attempts = 0
    while attempts < 3:
        start_point = random.sample(range(1, 9), 1)[0]
        mystery_point = random.sample(range(0, 5), 1)[0]
        sequence = [start_point * (start_point ** i) for i in range(6)]

        answer = sequence[mystery_point]
        output_sequence = ' '.join(map(str, sequence))
        mystery_sequence = output_sequence.replace(str(answer), "..", 1)

        print(f"Question: {mystery_sequence}")
        user_answer = int(input("Your answer: "))
        if user_answer == answer:
            print(f"Correct!\nCongratulation, {username}")
            break
        else:
            print(f"'{user_answer}' is wrong answer;(.Correct answer was '{answer}'.\n Let's try again, {username}!")
            attempts += 1
