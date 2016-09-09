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


def run_prediction(train_independent, train_dependent, test_independent, test_dependent):
    from sklearn import tree
    cart = tree.DecisionTreeRegressor()
    cart = cart.fit(train_independent, train_dependent)

    prediction = [float(x) for x in cart.predict(test_independent)]
    mre = []
    for i, j in zip(test_dependent, prediction):
        if i != 0:mre.append(abs(i - j) / abs(i))
        else: print "#"
    return round(sum(mre) / len(mre), 5) * 100


def get_ic(independent_samples, dependent_samples, n, epsilon=10):
    print ". ",
    sys.stdout.flush()

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
    return [h_measure, m_measure]


def wrapper_get_ic(filename):
    global distance_matrix
    divs = 200

    contents = pd.read_csv(filename)
    independent_columns = [c for c in contents.columns if "$<" not in c]
    independents = contents[independent_columns]
    dependent_column = [c for c in contents.columns if "$<" in c][-1]
    min_val_dependent = min(contents[dependent_column])
    max_val_dependent = max(contents[dependent_column])
    dependents = [(c - min_val_dependent)/(max_val_dependent - min_val_dependent) for c in contents[dependent_column]]


    distance_matrix = calculate_distance_matrix(independents)
    epsilon_range = max(dependents) - min(dependents)

    n = max(10, int(len(contents) * 0.1))
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
            dependent_samples.append(dependents[chosen_index])
        indexes.remove(chosen_index)

    test_independent = [independents.iloc[i] for i in indexes]
    test_dependent = [dependents[i] for i in indexes]

    x_axis = [(i * (epsilon_range/divs)) for i in xrange(1,divs)]
    y_axis = [get_ic(independent_samples,dependent_samples, n, epsilon=x) for x in x_axis]

    h_y_axis = [ya[0] for ya in y_axis]
    m_y_axis = [ya[1] for ya in y_axis]

    H_max = max(h_y_axis)
    settling_sensitivity = [i for i,h in enumerate(h_y_axis) if h < 0.05][0]
    M_0 = get_ic(independent_samples, dependent_samples, n, epsilon=0)[1]
    epsilon_half = max([x_axis[i] for i,m in enumerate(m_y_axis) if m > 0.5*M_0])

    # measuring epsilon star <- stability
    max_diff = max([abs(dependent_samples[i] - dependent_samples[i - 1]) for i in xrange(2, len(dependent_samples))])
    max_epsilon = [e for e in x_axis if e >= max_diff]
    print
    # print "Max Epsilon: ", max_epsilon[0]
    print "maximum information content: ", H_max,
    print "settling sensitivity: ", settling_sensitivity,
    print "initial partial information content: ", M_0,
    print "half partial information content point: ", epsilon_half
    print "Baseline Prediction: ", run_prediction(independent_samples,dependent_samples, test_independent, test_dependent)


    # import matplotlib.pyplot as plt
    # plt.plot(x_axis, y_axis)
    # # plt.ylim(-0.5, 1)
    # plt.show()

if __name__ == "__main__":
    files = ["../FeatureModels/" + f for f in listdir("../FeatureModels") if ".csv" in f]
    results = []
    print "apache"
    wrapper_get_ic("../FeatureModels/Apache.csv")
    print "sqlite"
    wrapper_get_ic("../FeatureModels/SQLite.csv")
    print "x264"
    wrapper_get_ic("../FeatureModels/BerkeleyDBJ.csv")
    # wrapper_get_ic("../TFeatureModels/no_interaction_apache.csv")
    # wrapper_get_ic("../TFeatureModels/twentyfive_interaction_apache.csv")
    # wrapper_get_ic("../TFeatureModels/fifty_interaction_apache.csv")
    # wrapper_get_ic("../TFeatureModels/one_hundred_interaction_apache.csv")
    # wrapper_get_ic("../TFeatureModels/two_hundred_interaction_apache.csv")