# Test optimizers on space trajectory problems

This repo does exactly what the name suggests.

The algorithms tested are not a exhaustive test of all available good algorithms. Rather, I performed a literature review, chose a subset A of algorithms to test and finally chose the ones I could find a good implementation available (of course what is a good implementation is biased, fee free to expand this work using other algorithms).

The algorithms were tested only on three distinct problems:

1. Going from Eath to Jupiter directly
2. Going from Earth to Jupiter doing a fly by through Mars
3. Cassini 1 problem

All those problems are solved with the same code made available by ESA. Feel free to expand the problem list and add other kind of problems.

## Solutions visualization
Open the jupyter notebooks in the root of this repository to visualize the trajectories of each input solution.

## Running optimizers
The optimizers tests and data visualization of the results are on the directory named `/optimizers`.

## Evaluating a input
The code that evaluates a given input to a problem was made available by ESA. It is inside the directory `/GTOPtoolbox`. I made small changes to that code so one can run the problems 1 and 2 cited above. Also, the CMake code was provided by me ;)
