from globals import problems
from generate_data import get_number_input_from_options
import pymoo_problems
from pymoo.algorithms.moo.nsga2 import NSGA2
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
        best_known = 9.3
        problem = pymoo_problems.Jupiter2(False)
    elif problem == 'Cassini 1':
        best_known = 5.1
        problem = pymoo_problems.Cassini1(False)

    algorithm = NSGA2()

    while True:
        result = minimize(problem, algorithm, verbose=False)
        X = result.X
        F = result.F[0]
        if type(F) == list:
            F = F[0]
        print(X)
        print(F)
        if F <= best_known:
            print(X)
            break
