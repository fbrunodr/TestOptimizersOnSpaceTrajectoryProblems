from globals import problems
from generate_data import get_number_input_from_options
import pymoo_problems
from pymoo.algorithms.soo.nonconvex.de import DE
from pymoo.optimize import minimize


if __name__ == '__main__':
    print('Choose problem')
    for i, problem in enumerate(problems):
        print(f'{i+1} {problem}')
    problem_idx = get_number_input_from_options([1,2,3])
    problem = problems[problem_idx-1]

    best_known = 1e9
    if problem == 'Jupiter Easy':
        best_known = 13.0
        problem = pymoo_problems.Jupiter1(False)
    elif problem == 'Jupiter Hard':
        best_known = 10.1
        problem = pymoo_problems.Jupiter2(False)
    elif problem == 'Cassini 1':
        best_known = 5.1
        problem = pymoo_problems.Cassini1(False)

    algorithm = DE()

    while True:
        result = minimize(problem, algorithm, verbose=False)
        if result.F.tolist()[0] <= best_known:
            print(result.X)
            break