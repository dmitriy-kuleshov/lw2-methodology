def welcome():
    print("Welcome to the Brain Games!")
    username = input("May I have your name?")
    print(f"Hello, {username}")
    return username


def attempt_quiz(username, question_func, correct_answer_func):
    attempts = 0
    while attempts < 3:
        question_data = question_func()
        correct_answer = correct_answer_func(question_data)

        print(f"Question: {question_data['formatted_question']}")
        assumption = int(input("Your answer: "))

        if assumption == correct_answer:
            print(f"Correct!\nCongratulation, {username}")
            break
        else:
            print(
                f"'{assumption}' is wrong answer;(. Correct answer was '{correct_answer}'.\nLet's try again, {username}!")
            attempts += 1
