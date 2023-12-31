from pathlib import Path
from sys import stdin
import matplotlib.pyplot as plt
import numpy as np
from aux_functions import get_algorithm_name, get_problem_name


def bar_plot_intervals(data: [float], intervals_lower_bound: [float], title: str, x_label: str, y_label: str) -> None:
    percentages = {}
    for i in range(len(intervals_lower_bound) - 1):
        percentages[f'{intervals_lower_bound[i]:.1f}'] = 0
    percentages[f'$\geq${intervals_lower_bound[-1]:.1f}'] = 0

    for val in data:
        for i in range(len(intervals_lower_bound) - 1):
            if intervals_lower_bound[i] <= val < intervals_lower_bound[i+1]:
                percentages[f'{intervals_lower_bound[i]:.1f}'] += 1
                break
        if val >= intervals_lower_bound[-1]:
            percentages[f'$\geq${intervals_lower_bound[-1]:.1f}'] += 1

    for key in percentages:
        percentages[key] *= 100 / len(data)

    jump = 1
    while len(intervals_lower_bound) // jump > 8:
        jump += 1
    ticks_to_show = list(range(0, len(intervals_lower_bound), jump))
    ticks_to_show.pop()
    ticks_to_show.append(len(intervals_lower_bound) - 1)

    # Plotting the bar chart
    plt.bar(percentages.keys(), percentages.values(), align='edge')
    plt.xlabel(x_label)
    plt.xticks(ticks_to_show)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid()
    plt.show()


def plot_evals(n_evals: [int], algorith_name: str, problem_name: str) -> None:
    bar_plot_intervals(
        [n_eval / 1000 for n_eval in n_evals],
        list(np.arange(0, 30.5, 1.0)),
        f'Number of evaluations of {algorith_name} on {problem_name}',
        'Thousands of evaluations',
        'Percentage of runs'
    )


def plot_best_delta_v(min_costs: [float], algorithm_name: str, problem_name: str) -> None:
    intervals = None
    if problem_name == 'Cassini 1':
        intervals = list(np.arange(5.0, 25.1, 0.5))
    elif problem_name == 'Jupiter Easy':
        intervals = list(np.arange(12.9, 20.01, 0.25))
    elif problem_name == 'Jupiter Hard':
        intervals = list(np.arange(9.4, 20.01, 0.25))
    bar_plot_intervals(
        min_costs,
        intervals,
        f'Best $\Delta$v of {algorithm_name} on {problem_name}',
        '$\Delta$v',
        'Percentage of runs'
    )


def show_single_objective_data(filePath: str) -> None:
    n_evals = []
    min_costs = []
    with open(filePath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            n_eval, min_cost = map(float, line.split(' '))
            n_evals.append(n_eval)
            min_costs.append(min_cost)
    algorithm_name = get_algorithm_name(filePath)
    problem_name = get_problem_name(filePath)
    plot_evals(n_evals, algorithm_name, problem_name)
    plot_best_delta_v(min_costs, algorithm_name, problem_name)


def plot_pareto_front(points: [[float]], algorithm_name: str, problem_name: str) -> None:
    best_solution_known = None
    file_name = f"data/{problem_name.replace(' ', '_').lower()}_pareto_points.txt"
    if Path.exists(Path(file_name)):
        with open(file_name) as file:
            best_solution_known = eval( file.readline() )

    deltaV = [point[0] for point in points]
    tf = [point[1] for point in points]
    plt.scatter(deltaV, tf, alpha=1/5)

    if best_solution_known is not None:
        deltaV = [point[0] for point in best_solution_known]
        tf = [point[1] for point in best_solution_known]
        plt.scatter(deltaV, tf, c='red', s=1.0)
        plt.legend([f'{algorithm_name} solutions', 'Best known solution'])

    plt.xlabel('$\Delta v$')
    plt.ylabel('$t_f$')
    plt.title(f'Union of solutions of {algorithm_name} on {problem_name} after 100 runs')
    plt.show()


def show_two_objective_data(filePath: str) -> None:
    n_evals = []
    pareto_points = []
    min_costs = []
    with open(filePath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            n_eval_part, list_part = line.split(' ', 1)
            n_eval = int(n_eval_part)
            n_evals.append(n_eval)
            points = eval(list_part)
            min_cost = 1e9
            for point in points:
                pareto_points.append(point)
                min_cost = min(min_cost, point[0])
            min_costs.append(min_cost)
    algorithm_name = get_algorithm_name(filePath)
    problem_name = get_problem_name(filePath)
    plot_evals(n_evals, algorithm_name, problem_name)
    plot_pareto_front(pareto_points, algorithm_name, problem_name)
    plot_best_delta_v(min_costs, algorithm_name, problem_name)


if __name__ == '__main__':
    dir_path = 'data'
    dir = Path(dir_path)

    file_list = list(dir.glob('*'))
    file_list.sort()

    print('Choose number to read file data:')
    for i, file in enumerate(file_list):
        print(f'{i+1}. {file}')

    file_idx = int(stdin.readline()) - 1
    file = file_list[file_idx]

    file = str(file)
    print(file)

    if 'single' in file:
        show_single_objective_data(file)
    else:
        show_two_objective_data(file)
