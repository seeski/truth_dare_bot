from random import choice


def get_truth():
    with open('truth_dare_questions/truth_questions.txt') as t:
        response = t.read().splitlines()
    return choice(response)

def get_dare():
    with open('truth_dare_questions/dare_questions.txt') as d:
        response = d.read().splitlines()
    return choice(response)

def get_random():
    return choice([get_truth(), get_dare()])