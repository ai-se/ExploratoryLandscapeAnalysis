from __future__ import division
import pandas as pd
import math
from random import shuffle, choice
from os import listdir
from sklearn.metrics import jaccard_similarity_score
import sys

global distance_matrix


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
    elif before == -1 and after == 1: return 2
    elif before == 0 and after == -1: return 3
    elif before == 0 and after == 1: return 4
    elif before == 1 and after == -1: return 5
    elif before == 1 and after == 0: return 6
    else: return 0


def get_ic(filename, epsilon=10):
    global distance_matrix
    print ". ",
    sys.stdout.flush()
    contents = pd.read_csv(filename)
    n = max(10, int(len(contents) * 0.1))
    independent_columns = [c for c in contents.columns if "$<" not in c]
    dependent_column = [c for c in contents.columns if "$<" in c][-1]
    independents = contents[independent_columns]
    dependents = contents[dependent_column]

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
    independent_sequence = [independent_samples[start_index]]
    dependent_sequence = [dependent_samples[start_index]]
    indexes.remove(start_index)

    while len(independent_sequence) <= n:
        nearest_indexes = sorted([[i, distance(independent_sequence[-1], independent_samples[i])] for i in indexes], key=lambda x:x[1])[0][0]
        independent_sequence.append(independent_samples[nearest_indexes])
        dependent_sequence.append(dependent_samples[nearest_indexes])
        indexes.remove(nearest_indexes)

    # make pairs
    pairs = []
    for i in xrange(len(independent_sequence) - 1):
        diff = (dependent_sequence[i+1] - dependent_sequence[i])/distance(independent_sequence[i+1], independent_sequence[i])
        if diff < -1 * epsilon: pairs.append(-1)
        elif abs(diff) <= epsilon: pairs.append(0)
        elif diff > epsilon: pairs.append(1)
        else: assert(False)

    for_probability = [get_sequence_number(pairs[i], pairs[i+1]) for i in xrange(len(pairs) - 1)]

    prob_scores = [for_probability.count(i)/len(for_probability) for i in xrange(1, 7)]
    h_measure = sum([-1 * p * math.log(p, 6) for p in prob_scores if p!=0])


    # for m measure

    # Remove all zeroes
    zero_removed_pairs = [p for p in pairs if p != 0]

    repeated_removed_pairs = []
    # Remove all repeated elements
    for i in xrange(len(zero_removed_pairs) - 1):
        if zero_removed_pairs[i] != zero_removed_pairs[i+1]:
            repeated_removed_pairs.append(zero_removed_pairs[i])

    m_measure = len(repeated_removed_pairs)/(len(pairs)-1)
    # print ">> ", dependent_sequence
    # print pairs
    # print h_measure
    # print
    return h_measure


def wrapper_get_ic(filename):
    global distance_matrix
    divs = 100

    contents = pd.read_csv(filename)
    independent_columns = [c for c in contents.columns if "$<" not in c]
    independents = contents[independent_columns]
    dependent_column = [c for c in contents.columns if "$<" in c][-1]
    dependents = contents[dependent_column]

    distance_matrix = calculate_distance_matrix(independents)
    epsilon_range = max(dependents) - min(dependents)
    x_axis = [(i * (epsilon_range/divs)) for i in xrange(1,divs)]
    y_axis = [get_ic(filename, epsilon=x) for x in x_axis]

    import matplotlib.pyplot as plt
    plt.plot(x_axis, y_axis)
    plt.ylim(-0.5, 1)
    plt.show()

if __name__ == "__main__":
    files = ["../FeatureModels/" + f for f in listdir("../FeatureModels") if ".csv" in f]
    results = []
    wrapper_get_ic("../FeatureModels/Apache.csv")