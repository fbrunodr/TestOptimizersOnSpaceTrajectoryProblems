from sys import stdin
from globals import problems, algorithms
from get_best_and_evals import get_best_and_evals
from aux_functions import get_number_input_from_options


if __name__ == '__main__':
    print('Choose problem')
    for i, problem in enumerate(problems):
        print(f'{i+1} {problem}')

    problem_idx = get_number_input_from_options(list(range(1, len(problems)+1)))
    problem = problems[problem_idx - 1]

    print('\nChoose algorithm:')
    for i, algorithm in enumerate(algorithms):
        print(f'{i+1} {algorithm}')

    algorithm_idx = get_number_input_from_options(list(range(1, len(algorithms)+1)))
    algorithm = algorithms[algorithm_idx - 1]

    optimize_end_time = False

    if algorithm_idx in [6, 8, 9]:
        optimize_end_time = True
    elif algorithm_idx == 7:
        print('\nMinimize mission end time? [y/N]')
        answer = stdin.readline().strip()
        if answer.lower() == 'y':
            optimize_end_time = True

    file_name = f"data/{problem.replace(' ', '_').lower()}_{algorithm.replace('/', '').lower()}_{'multi_objective' if optimize_end_time else 'single_objective'}.txt"

    curr_n_lines = 0
    try:
        with open(file_name, 'r+') as file:
            curr_n_lines = len(file.readlines())
    except:
        pass

    with open(file_name, 'a+') as file:
        for i in range(curr_n_lines + 1, 101):
            min_cost, evals = get_best_and_evals(problem, algorithm, optimize_end_time)
            if not optimize_end_time:
                while type(min_cost) == list:
                    min_cost = min_cost[0]
            file.write(f'{evals} {min_cost}\n')
            print(f'Wrote line {i}/100')
