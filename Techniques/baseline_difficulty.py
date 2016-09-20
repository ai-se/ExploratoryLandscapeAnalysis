from __future__ import division
import pandas as pd
import numpy as np
from random import shuffle
from os import listdir

class holder():
    def __init__(self, filename, difficulty, points):
        self.filename = filename
        self.difficulty = difficulty
        self.points = points

    def __str__(self):
        return self.filename + ", " + str(self.difficulty) + ", " + str(self.points)

def euclidean_distance(list1, list2):
    assert(len(list1) == len(list2)), "The points don't have the same dimension"
    distance = sum([(i - j) ** 2 for i, j in zip(list1, list2)]) ** 0.5
    assert(distance >= 0), "Distance can't be less than 0"
    return distance


def get_baseline_for_min(filename):
    """ Lower the value...simpler it is"""
    contents = pd.read_csv(filename)
    n = max(10, int(0.1 * len(contents)))
    independent_columns = [c for c in contents.columns if "$<" not in c]
    dependent_column = [c for c in contents.columns if "$<" in c][-1]
    independents = contents[independent_columns]
    dependents = contents[dependent_column]

    indexes = range(len(contents))
    shuffle(indexes)
    samples = indexes[:n]
    independent_values = [independents.iloc[i] for i in samples]
    dependent_values = [dependents.iloc[i] for i in samples]
    assert(len(independent_values) == len(dependent_values)), "sanity check failed"

    best_random_solution = sorted(dependent_values)[0]
    best_actual_solution = sorted(dependents.tolist())[0]
    max_difference = abs(sorted(dependents.tolist())[-1] - sorted(dependents.tolist())[0])

    return [round(abs(best_actual_solution - best_random_solution)/max_difference, 4), n]


def get_baseline_for_max(filename, n=100):
    """ Lower the value...simpler it is"""
    contents = pd.read_csv(filename)
    n = min(n, int(0.1 * len(contents)))
    independent_columns = [c for c in contents.columns if "$<" not in c]
    dependent_column = [c for c in contents.columns if "$<" in c][-1]
    independents = contents[independent_columns]
    dependents = contents[dependent_column]

    indexes = range(len(contents))
    shuffle(indexes)
    samples = indexes[:n]
    independent_values = [independents.iloc[i] for i in samples]
    dependent_values = [dependents.iloc[i] for i in samples]
    assert(len(independent_values) == len(dependent_values)), "sanity check failed"

    best_random_solution = sorted(dependent_values)[-1]
    best_actual_solution = sorted(dependents.tolist())[-1]
    max_difference = abs(sorted(dependents.tolist())[-1] - sorted(dependents.tolist())[0])

    return [round(abs(best_actual_solution - best_random_solution)/max_difference, 4), n]

if __name__ == "__main__":
    # files = ["../FeatureModels/" + f for f in listdir("../FeatureModels") if ".csv" in f]
    files = [
                "../FeatureModels/Apache.csv",
                "../FeatureModels/SQLite.csv",
                "../FeatureModels/x264.csv",
             ]
    results = []
    for file in files:
        temp = [get_baseline_for_min(file) for _ in xrange(10)]
        # temp = [get_baseline_for_max(file) for _ in xrange(10)]
        results.append(holder(file.split("/")[-1], np.mean([c[0] for c in temp]), np.mean([c[-1] for c in temp])))
    for s in sorted(results, key=lambda x:x.difficulty, reverse=True): print s
