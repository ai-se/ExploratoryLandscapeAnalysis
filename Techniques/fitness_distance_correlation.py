from __future__ import division
import pandas as pd
import numpy as np
from random import shuffle
from os import listdir


def euclidean_distance(list1, list2):
    assert(len(list1) == len(list2)), "The points don't have the same dimension"
    distance = sum([(i - j) ** 2 for i, j in zip(list1, list2)]) ** 0.5
    assert(distance >= 0), "Distance can't be less than 0"
    return distance


def get_fdc(filename, n=10):
    contents = pd.read_csv(filename)
    independent_columns = [c for c in contents.columns if "$<" not in c]
    dependent_column = [c for c in contents.columns if "$<" in c][-1]
    independents = contents[independent_columns]
    dependents = contents[dependent_column]

    indexes = range(len(contents))
    shuffle(indexes)

    # n = 100#min(n, int(len(contents) * 0.1))
    samples = indexes[:n]
    independent_values = [independents.iloc[i] for i in samples]
    dependent_values = [dependents.iloc[i] for i in samples]
    assert(len(independent_values) == len(dependent_values)), "sanity check failed"

    global_optima_index = dependents.tolist().index(min(dependents))
    independent_global_optima = independents.iloc[global_optima_index]
    distance_list = [euclidean_distance(point, independent_global_optima) for point in independent_values]

    mean_distance = np.mean(distance_list)
    mean_fitness = np.mean(dependent_values)
    std_distance = np.std(distance_list)
    std_fitness = np.std(dependent_values)

    measure = 0
    for i in xrange(n):
        measure += (distance_list[i] - mean_distance) * (dependent_values[i] - mean_fitness)
    measure /= (n * std_distance * std_fitness)
    return measure

if __name__ == "__main__":
    files = ["../FeatureModels/" + f for f in listdir("../FeatureModels") if ".csv" in f]
    for file in files:
        print file,
        print np.mean([get_fdc(file, n=100) for _ in xrange(10)])