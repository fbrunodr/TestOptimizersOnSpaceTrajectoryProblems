from objective_functions import *
from pymoo.core.problem import Problem
import numpy as np
from multiprocessing import Pool    


class Jupiter1(Problem):
    def __init__(self, include_end_time=False):
        number_of_objectives = 2 if include_end_time else 1
        super().__init__(
            n_var=2, n_obj=number_of_objectives, n_constr=0,
            xl=np.array([9131.5, 200.0]),
            xu=np.array([9495.5, 1500.0])
        )

    def _evaluate(self, x, out, *args, **kwargs):
        pool = Pool(processes=8)
        if self.n_obj == 1:
            out["F"] = pool.map(jupiter1_single_objective, x)
        elif self.n_obj == 2:
            out["F"] = pool.map(jupiter1_multi_objective, x)
        pool.close()
        pool.join()


class Jupiter2(Problem):
    def __init__(self, include_end_time=False):
        number_of_objectives = 2 if include_end_time else 1
        super().__init__(
            n_var=4, n_obj=number_of_objectives, n_constr=0,
            xl=np.array([9131.5, 50.0, 50.0, 50.0]),
            xu=np.array([10591.5, 1000.0, 1000.0, 1500.0])
        )

    def _evaluate(self, x, out, *args, **kwargs):
        pool = Pool(processes=8)
        if self.n_obj == 1:
            out["F"] = pool.map(jupiter2_single_objective, x)
        elif self.n_obj == 2:
            out["F"] = pool.map(jupiter2_multi_objective, x)
        pool.close()
        pool.join()


class Cassini1(Problem  ):
    def __init__(self, include_end_time=False):
        number_of_objectives = 2 if include_end_time else 1
        super().__init__(
            n_var=6, n_obj=number_of_objectives, n_constr=0,
            xl=np.array([-1000.0, 30.0, 100.0, 30.0, 400.0, 1000.0]),
            xu=np.array([0.0, 400.0, 470.0, 400.0, 2000.0, 6000.0])
        )

    def _evaluate(self, x, out, *args, **kwargs):
        pool = Pool(processes=8)
        if self.n_obj == 1:
            out["F"] = pool.map(cassini1_single_objective, x)
        elif self.n_obj == 2:
            out["F"] = pool.map(cassini1_multi_objective, x)
        pool.close()
        pool.join()
