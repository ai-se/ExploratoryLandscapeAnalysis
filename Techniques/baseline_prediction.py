from __future__ import division
from sklearn import tree
from random import shuffle
import pandas as pd

def run_cart(filename, n=10):
    contents = pd.read_csv(filename)
    independent_columns = [c for c in contents.columns if "$<" not in c]
    independents = contents[independent_columns]
    dependent_column = [c for c in contents.columns if "$<" in c][-1]
    dependent = contents[dependent_column]

    indexes = range(len(contents))
    shuffle(indexes)
    number_of_points = max(10, int(len(contents) * 0.1))
    train_indexes = indexes[:number_of_points]
    test_indexes = indexes[number_of_points:]

    train_independent = [independents.iloc[i] for i in train_indexes]
    train_dependent = [dependent.iloc[i] for i in train_indexes]

    test_independent = [independents.iloc[i] for i in test_indexes]
    test_dependent = [dependent.iloc[i] for i in test_indexes]

    cart = tree.DecisionTreeRegressor()
    cart = cart.fit(train_independent, train_dependent)

    prediction = [float(x) for x in cart.predict(test_independent)]
    mre = []
    for i, j in zip(test_dependent, prediction):
        mre.append(abs(i - j)/ abs(i))
    return round(sum(mre)/len(mre), 5) * 100

if __name__ == "__main__":
    files = [
        "../FeatureModels/Apache.csv",
        "../FeatureModels/SQLite.csv",
        "../FeatureModels/x264.csv",
    ]
    for file in files:
        print run_cart(file)

