import random


def welcome():
    print("Welcome to the Brain Games!\n" "May I have your name?")
    name = input()
    return f"Hello, {name}!"


def lcm_alg():
    print("Find the smallest common multiple of given numbers.")
    numbers = random.sample(range(0, 500), 3)
    return numbers
