from objective_functions import *
from pymoo.core.problem import Problem
import numpy as np


class Jupiter1(Problem):
    def __init__(self, include_end_time=False):
        number_of_objectives = 2 if include_end_time else 1
        super().__init__(
            n_var=2, n_obj=number_of_objectives, n_constr=0,
            xl=np.array([9131.5, 300.0]),
            xu=np.array([9495.5, 3000.0])
        )

    def _evaluate(self, x, out, *args, **kwargs):
        if self.n_obj == 1:
            out["F"] = np.apply_along_axis(jupiter1_single_objective, 1, x)
        elif self.n_obj == 2:
            out["F"] = np.apply_along_axis(jupiter1_multi_objective, 1, x)


class Jupiter2(Problem):
    def __init__(self, include_end_time=False):
        number_of_objectives = 2 if include_end_time else 1
        super().__init__(
            n_var=3, n_obj=number_of_objectives, n_constr=0,
            xl=np.array([9131.5, 50.0, 300.0]),
            xu=np.array([10958, 1000.0, 3000.0])
        )

    def _evaluate(self, x, out, *args, **kwargs):
        if self.n_obj == 1:
            out["F"] = np.apply_along_axis(jupiter2_single_objective, 1, x)
        elif self.n_obj == 2:
            out["F"] = np.apply_along_axis(jupiter2_multi_objective, 1, x)


class Cassini1(Problem  ):
    def __init__(self, include_end_time=False):
        number_of_objectives = 2 if include_end_time else 1
        super().__init__(
            n_var=6, n_obj=number_of_objectives, n_constr=0,
            xl=np.array([-1000.0, 30.0, 100.0, 30.0, 400.0, 1000.0]),
            xu=np.array([0.0, 400.0, 470.0, 400.0, 2000.0, 6000.0])
        )

    def _evaluate(self, x, out, *args, **kwargs):
        if self.n_obj == 1:
            out["F"] = np.apply_along_axis(cassini1_single_objective, 1, x)
        elif self.n_obj == 2:
            out["F"] = np.apply_along_axis(cassini1_multi_objective, 1, x)
