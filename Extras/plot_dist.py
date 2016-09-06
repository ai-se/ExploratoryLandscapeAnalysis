from __future__ import division
import pandas as pd
import numpy as np
from random import shuffle, random
from sklearn import tree
from os import listdir


def get_cross_eval(filename, n=100):
    results = []
    contents = pd.read_csv(filename)
    independent_columns = [c for c in contents.columns if "$<" not in c]
    dependent_column = [c for c in contents.columns if "$<" in c][-1]
    independents = contents[independent_columns]
    dependents = contents[dependent_column]

    graph_name = filename.split("/")[-1]
    import matplotlib.pyplot as plt
    plt.hist(dependents)
    plt.title(graph_name)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig("./Figures/" + graph_name[:-3]+".png")
    plt.cla()

if __name__ == "__main__":

    files = ["../FeatureModels/" + f for f in listdir("../FeatureModels") if ".csv" in f]
    for file in files:
        get_cross_eval(file)
