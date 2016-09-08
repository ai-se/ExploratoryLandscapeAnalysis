from __future__ import division
import pandas as pd
import numpy as np
from random import shuffle, choice
from os import listdir
from sklearn.metrics import jaccard_similarity_score


def distance(lista, listb):
    return jaccard_similarity_score(lista, listb, normalize=False)


def calculate_distance_matrix(independents):
    distances = [[-1 for _ in xrange(len(independents))] for _ in xrange(len(independents))]
    for i in xrange(len(independents)):
        for j in xrange(len(independents)):
            if i == j:
                distances[i][j] = 0
            elif distances[i][j] == -1:
                distances[i][j] = distance(independents.iloc[i], independents.iloc[j])
                distances[j][i] = distances[i][j]
    return distances


def get_sequence_number(before, after):
    if before == -1 and after == 0: return 1
    if before == -1 and after == 1: return 2
    if before == 0 and after == -1: return 3
    if before == 0 and after == 1: return 4
    if before == 1 and after == -1: return 5
    if before == 1 and after == 0: return 6


def get_ic(filename, epsilon=10):
    contents = pd.read_csv(filename)
    n = max(10, int(len(contents) * 0.1))
    independent_columns = [c for c in contents.columns if "$<" not in c]
    dependent_column = [c for c in contents.columns if "$<" in c][-1]
    independents = contents[independent_columns]
    dependents = contents[dependent_column]

    distance_matrix = calculate_distance_matrix(independents)
    max_distance = max([max(d) for d in distance_matrix])

    indexes = range(len(independents))
    shuffle(indexes)
    independent_samples = []
    dependent_samples = []
    step_size = int(max_distance * 0.1)
    while len(independent_samples) <= n:
        chosen_index = choice(indexes)
        choosen = independents.iloc[chosen_index]
        min_distance = [distance(choosen, other) for other in independent_samples]
        if min_distance > step_size:
            independent_samples.append(choosen)
            dependent_samples.append(dependents.iloc[chosen_index])
        indexes.remove(chosen_index)

    # build sequence
    indexes = range(len(independent_samples))
    start_index = choice(indexes)
    indepenent_sequence = [independent_samples[start_index]]
    dependent_sequence = [dependent_samples[start_index]]
    indexes.remove(start_index)

    while len(indepenent_sequence) <= n:
        nearest_indexes = sorted([[i, distance(indepenent_sequence[-1], independent_samples[i])] for i in indexes], key=lambda x:x[1])[0][0]
        indepenent_sequence.append(independent_samples[nearest_indexes])
        dependent_sequence.append(dependent_samples[nearest_indexes])
        indexes.remove(nearest_indexes)

    # make pairs
    pairs = []
    for i in xrange(len(indepenent_sequence) - 1):
        diff = dependent_sequence[i+1] - dependent_sequence[i]
        if diff < -1 * epsilon: pairs.append(-1)
        elif abs(diff) <= epsilon: pairs.append(0)
        elif diff > epsilon: pairs.append(1)
        else: assert(False)



    import pdb
    pdb.set_trace()


if __name__ == "__main__":
    files = ["../FeatureModels/" + f for f in listdir("../FeatureModels") if ".csv" in f]
    results = []
    print get_ic("../FeatureModels/Apache.csv")