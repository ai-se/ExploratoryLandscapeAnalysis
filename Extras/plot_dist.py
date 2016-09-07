from __future__ import division
import pandas as pd
import numpy as np
from random import shuffle, random
from sklearn import tree
from os import listdir


def euclidean_distance(list1, list2):
    assert(len(list1) == len(list2)), "The points don't have the same dimension"
    distance = sum([(i - j) ** 2 for i, j in zip(list1, list2)]) ** 0.5
    assert(distance >= 0), "Distance can't be less than 0"
    return distance


def find_distance(filename):
    results = []
    contents = pd.read_csv(filename)
    independent_columns = [c for c in contents.columns if "$<" not in c]
    dependent_column = [c for c in contents.columns if "$<" in c][-1]
    independents = contents[independent_columns]
    dependents = contents[dependent_column]

    distances = [[[-1, -1] for _ in xrange(len(independents))] for _ in xrange(len(independents))]
    for i in xrange(len(independents)):
        for j in xrange(len(independents)):
            if i==j:
                distances[i][j][0] = 0
                distances[i][j][1] = 0
            elif distances[i][j][0] == -1:
                distances[i][j][0] = euclidean_distance(independents.iloc[i], independents.iloc[j])
                distances[i][j][1] = abs(dependents[i] - dependents[j])
                distances[j][i][0] = distances[i][j][0]
                distances[j][i][1] = distances[i][j][1]

    lista = []
    listb = []
    print [d[1] for d in distances[0] if d[0]==1]

if __name__ == "__main__":

    find_distance("../FeatureModels/Apache.csv")
