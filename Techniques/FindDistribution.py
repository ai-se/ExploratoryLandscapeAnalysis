from __future__ import division
import pandas as pd
import numpy as np
from random import shuffle
from os import listdir
from sklearn import tree


def get_cross_eval(filename, n=100):
    results = []
    contents = pd.read_csv(filename)
    independent_columns = [c for c in contents.columns if "$<" not in c]
    dependent_column = [c for c in contents.columns if "$<" in c][-1]
    independents = contents[independent_columns]
    dependents = contents[dependent_column]

    indexes = range(len(contents))
    shuffle(indexes)

    n = min(n, int(len(contents) * 0.1))
    samples = indexes[:n]
    independent_values = [independents.iloc[i] for i in samples]
    dependent_values = [dependents.iloc[i] for i in samples]
    assert(len(independent_values) == len(dependent_values)), "sanity check failed"

    graph_name = filename.split("/")[-1]
    import matplotlib.pyplot as plt
    plt.hist(dependent_values)
    plt.title(graph_name)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig("../Figures/Distribution/" + graph_name[:-4]+".png")
    plt.cla()

if __name__ == "__main__":

    files = ["../FeatureModels/" + f for f in listdir("../FeatureModels") if ".csv" in f]
    for file in files:
        get_cross_eval(file)