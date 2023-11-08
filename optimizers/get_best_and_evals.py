from globals import problems, algorithms, multi_objective_algorithms, single_objective_algorithms

# pymoo solvers
from pymoo.algorithms.soo.nonconvex.pso import PSO
from pymoo.algorithms.soo.nonconvex.de import DE
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.algorithms.moo.moead import MOEAD
from pymoo.util.ref_dirs import get_reference_directions
from pymoo.optimize import minimize
import pymoo_problems

import pygmo as pg
import pygmo_problems


def get_best_and_evals(problem: str, algorithm: str, optimize_end_time: bool) -> [float, float]:
    assert problem in problems
    assert algorithm in algorithms

    if optimize_end_time:
        assert algorithm in multi_objective_algorithms
    else:
        assert algorithm in single_objective_algorithms

    algorithms_available_in_pymoo = ['PSO', 'DE', 'GA', 'NSGA-II', 'MOEA/D']
    if algorithm in algorithms_available_in_pymoo:
        return _solve_using_pymoo(problem, algorithm, optimize_end_time)
    else:
        return _solve_using_pygmo(problem, algorithm, optimize_end_time)


def _solve_using_pymoo(problem: str, algorithm: str, optimize_end_time: bool) -> [float, float]:
    if problem == problems[0]:
        problem = pymoo_problems.Jupiter1(optimize_end_time)
    elif problem == problems[1]:
        problem = pymoo_problems.Jupiter2(optimize_end_time)
    elif problem == problems[2]:
        problem = pymoo_problems.Cassini1(optimize_end_time)

    if algorithm == 'PSO':
        algorithm = PSO()
    elif algorithm == 'DE':
        algorithm = DE()
    elif algorithm == 'GA':
        algorithm = GA()
    elif algorithm == 'NSGA-II':
        algorithm = NSGA2()
    elif algorithm == 'MOEA/D':
        ref_dirs = get_reference_directions("uniform", 2, n_partitions=24)
        algorithm = MOEAD(ref_dirs, n_neighbors=15, prob_neighbor_mating=0.7)

    result = minimize(problem, algorithm, verbose=False)
    return result.F.tolist(), result.algorithm.evaluator.n_eval


def _solve_using_pygmo(problem: str, algorithm: str, optimize_end_time: bool) -> [float, float]:
    if problem == problems[0]:
        problem = pg.problem(pygmo_problems.Jupiter1(optimize_end_time))
    elif problem == problems[1]:
        problem = pg.problem(pygmo_problems.Jupiter2(optimize_end_time))
    elif problem == problems[2]:
        problem = pg.problem(pygmo_problems.Cassini1(optimize_end_time))

    population = pg.population(problem, size = 256)

    if algorithm == 'SA':
        algorithm = pg.algorithm(pg.simulated_annealing())
    elif algorithm == 'ABC':
        algorithm = pg.algorithm(pg.bee_colony())
    elif algorithm == 'MOPSO':
        algorithm = pg.algorithm(pg.nspso())
    elif algorithm == 'MHACO':
        algorithm = pg.algorithm(pg.maco())

    population = algorithm.evolve(population)
    if not optimize_end_time:
        best_fitness = population.get_f()[population.best_idx()].tolist()
        return best_fitness, population.problem.get_fevals()
    else:
        fronts_2d = pg.non_dominated_front_2d(population.get_f())
        best_individuals_2d = [population.get_f()[i].tolist() for i in fronts_2d]
        return best_individuals_2d, population.problem.get_fevals()
