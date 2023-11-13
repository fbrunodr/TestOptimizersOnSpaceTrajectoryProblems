from globals import *
from sys import stdin


def get_problem_name(filePath: str) -> str:
    for problem in problems:
        if problem.replace(' ', '_').lower() in filePath:
            return problem
    return ''


def get_algorithm_name(filePath: str) -> str:
    # reversed is here to avoid NSGA-II being mistaken for GA and MOPSO for PSO
    for algorithm in reversed(algorithms):
        if algorithm.replace('/', '').lower() in filePath:
            return algorithm
    return ''


def get_number_input_from_options(valid_options: [int]) -> int:
    try:
        number = int(stdin.readline())
        if number not in valid_options:
            raise ValueError('Number not in options')
        return number
    except:
        print(f'Invalid input... try again.')
        return get_number_input_from_options(valid_options)
