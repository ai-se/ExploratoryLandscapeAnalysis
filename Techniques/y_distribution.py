from __future__ import division
from scipy.stats import skew, kurtosis
import pandas as pd
from random import shuffle
import numpy as np
from os import listdir

class holder():
    def __init__(self, filename, skew, kurtosis):
        self.filename = filename
        self.skew = skew
        self.kurtosis = kurtosis

    def __str__(self):
        return self.filename + ", " + str(self.skew) + ", " + str(self.kurtosis)

def get_ydist(filename, n = 100):
    results = []
    contents = pd.read_csv(filename)
    independent_columns = [c for c in contents.columns if "$<" not in c]
    dependent_column = [c for c in contents.columns if "$<" in c][-1]
    independents = contents[independent_columns]
    dependents = contents[dependent_column]

    indexes = range(len(contents))
    shuffle(indexes)
    samples = np.array(indexes[:n])
    independent_values = [independents.iloc[i] for i in samples]
    dependent_values = [dependents.iloc[i] for i in samples]
    assert(len(independent_values) == len(dependent_values)), "sanity check failed"
    return round(skew(dependent_values), 4), round(kurtosis(dependent_values, fisher=False), 4)

if __name__ == "__main__":
    results = []
    files = ["../FeatureModels/" + f for f in listdir("../FeatureModels") if ".csv" in f]
    for file in files:
        mean, std = get_ydist(file)
        results.append(holder(file.split("/")[-1], mean, std))
    sort = sorted(results, key=lambda x:x.skew, reverse=True)
    for s in sort: print s