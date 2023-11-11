from globals import problems
from aux_functions import get_number_input_from_options, get_problem_name
from pathlib import Path
import matplotlib.pyplot as plt


def get_pareto_front_2d(points: [[float]]):
    pareto_front = []

    for i in range(len(points)):
        i_is_optimial = True
        for j in range(len(points)):
            if i == j:
                continue
            A = points[i]
            B = points[j]

            if (B[0] == A[0]) and (B[1] == A[1]) and j > i:
                continue

            if (B[0] <= A[0]) and (B[1] <= A[1]):
                i_is_optimial = False
                break

        if i_is_optimial:
            pareto_front.append(points[i])

    return pareto_front


def get_results(filePath: str) -> [[float]]:
    pareto_points = []
    with open(filePath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            n_eval_part, list_part = line.split(' ', 1)
            points = eval(list_part)
            for point in points:
                pareto_points.append(point)
    return get_pareto_front_2d(pareto_points)


if __name__ == '__main__':
    print('Choose problem')
    for i, problem in enumerate(problems):
        print(f'{i+1} {problem}')

    i = get_number_input_from_options([1, 2, 3])
    problem = problems[i-1]

    dir_path = 'data'
    dir = Path(dir_path)
    file_list = list(dir.glob('*'))

    pareto_front = []

    for file in file_list:
        if file.suffix != '.txt':
            continue
        file = str(file)
        problem_name = get_problem_name(file)
        if problem_name != problem:
            continue
        if 'multi_objective' not in file:
            continue
        collected_points = get_results(file)
        for point in collected_points:
            pareto_front.append(point)
        pareto_front = get_pareto_front_2d(pareto_front)

    pareto_front.sort()

    deltaV = [point[0] for point in pareto_front]
    tf = [point[1] for point in pareto_front]
    plt.scatter(deltaV, tf, alpha=1/5)
    plt.xlabel('$\Delta v$')
    plt.ylabel('$t_f$')
    plt.title('Pareto points')
    plt.show()

    save_file = f"data/{problem.replace(' ', '_').lower()}_pareto_points.txt"
    with open(save_file, 'w') as file:
        file.write(str(pareto_front))
