from __future__ import division
import pandas as pd
import numpy as np
from random import shuffle, random
from sklearn import tree
from os import listdir

class holder():
    def __init__(self, filename, mean, std):
        self.filename = filename
        self.mean = mean
        self.std = std

    def __str__(self):
        return self.filename + ", " + str(self.mean) + ", " + str(self.std)

def get_cross_eval(filename, n=100):
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

    # perform a 10 way cross eval
    from sklearn.cross_validation import KFold
    kf = KFold(len(independent_values), n_folds=10)
    for train, test in kf:
        X_train = [independent_values[i] for i in train]
        X_test = [independent_values[i] for i in test]
        y_train = [dependent_values[i] for i in train]
        y_test = [dependent_values[i] for i in test]
        CART = tree.DecisionTreeRegressor()
        CART = CART.fit(X_train, y_train)

        prediction = CART.predict(X_test)

        mre = []
        for i, j in zip(y_test, prediction):
            mre.append(abs(i - j)/float(i))
        results.append(sum(mre)/len(mre))

    return round(np.mean(results) * 100, 3), round(np.std(results) * 100, 3)


if __name__ == "__main__":
    results = []
    files = ["../FeatureModels/" + f for f in listdir("../FeatureModels") if ".csv" in f]
    for file in files:
        mean, std = get_cross_eval(file)
        results.append(holder(file.split("/")[-1], mean, std))
    sort = sorted(results, key=lambda x:x.mean, reverse=True)
    for s in sort: print s