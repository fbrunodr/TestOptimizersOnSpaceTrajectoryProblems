import subprocess


def jupiter1_single_objective(x: [float]) -> float:
    values = list(map(str, x))
    cpp_binary = "../GTOPtoolbox/build/jupiter1Main"
    return float(subprocess.run([cpp_binary] + values, stdout=subprocess.PIPE, text=True).stdout)


def jupiter1_multi_objective(x: [float]) -> [float]:
    return [jupiter1_single_objective(x), sum(x)]


def jupiter2_single_objective(x: [float]) -> float:
    values = list(map(str, x))
    cpp_binary = "../GTOPtoolbox/build/jupiter2Main"
    return float(subprocess.run([cpp_binary] + values, stdout=subprocess.PIPE, text=True).stdout)


def jupiter2_multi_objective(x: [float]) -> [float]:
    return [jupiter2_single_objective(x), sum(x)]


def cassini1_single_objective(x: [float]) -> float:
    values = list(map(str, x))
    cpp_binary = "../GTOPtoolbox/build/cassini1Main"
    return float(subprocess.run([cpp_binary] + values, stdout=subprocess.PIPE, text=True).stdout)


def cassini1_multi_objective(x: [float]) -> [float]:
    return [cassini1_single_objective(x), sum(x)]
