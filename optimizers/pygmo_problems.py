from objective_functions import *


class Jupiter1:
    def __init__(self, include_end_time) -> None:
        self.include_end_time = include_end_time

    def get_nobj(self):
        return 2 if self.include_end_time else 1

    def fitness(self, x):
        if self.include_end_time:
            return jupiter1_multi_objective(x)
        else:
            return [jupiter1_single_objective(x)]

    def get_bounds(self):
        return ([9131.5, 300.0],[9495.5, 3000.0])


class Jupiter2:
    def __init__(self, include_end_time) -> None:
        self.include_end_time = include_end_time

    def get_nobj(self):
        return 2 if self.include_end_time else 1

    def fitness(self, x):
        if self.include_end_time:
            return jupiter2_multi_objective(x)
        else:
            return [jupiter2_single_objective(x)]

    def get_bounds(self):
        return ([9131.5, 50.0, 300.0],[10958, 1000.0, 3000.0])


class Cassini1:
    def __init__(self, include_end_time) -> None:
        self.include_end_time = include_end_time

    def get_nobj(self):
        return 2 if self.include_end_time else 1

    def fitness(self, x):
        if self.include_end_time:
            return cassini1_multi_objective(x)
        else:
            return [cassini1_single_objective(x)]

    def get_bounds(self):
        return (
            [-1000.0, 30.0, 100.0, 30.0, 400.0, 1000.0],
            [0.0, 400.0, 470.0, 400.0, 2000.0, 6000.0]
        )
