from __future__ import division
import pandas as pd
from sklearn.ensemble.forest import RandomForestRegressor
import numpy as np
import sys


def get_prediction_error(train, test):

    assert(len(train.columns) == len(test.columns)), "Something is wrong"
    columns = train.columns

    indep_columns = [c for c in columns if "<$" not in c]

    train_independent = train[indep_columns]
    train_dependent_obj1 = train['<$IDem_Decision']
    train_dependent_obj2 = train['<$IDem_Objective']

    test_independent = test[indep_columns]
    test_dependent_obj1 = train['<$IDem_Decision']
    test_dependent_obj2 = train['<$IDem_Objective']

    model1 = RandomForestRegressor(n_estimators=100)
    model1.fit(train_independent, train_dependent_obj1)

    model2 = RandomForestRegressor(n_estimators=100)
    model2.fit(train_independent, train_dependent_obj2)

    prediction_obj1 = model1.predict(test_independent)
    prediction_obj2 = model2.predict(test_independent)


    mre_obj1 = [100*(abs(i-j)/j) for i, j in zip(prediction_obj1, test_dependent_obj1)]
    mre_obj2 = [100*(abs(i-j)/j) for i, j in zip(prediction_obj2, test_dependent_obj2)]
    print ".",
    sys.stdout.flush()

    return [round(np.mean(mre_obj1), 3), round(np.mean(mre_obj2), 3)]


def getn_way(filename):
    def extract_name(dsname):
        position_underscore = [pos for pos, char in enumerate(dsname) if char == "_"][-1]
        majorname = dsname[:position_underscore].split("/")[-1]
        return majorname

    content = pd.read_csv(filename)
    dataset_column = [c for c in content.columns if "$$" in c][-1]
    dataset_names = [content[dataset_column].iloc[i] for i in xrange(len(content))]
    datasets = list(set([extract_name(dsn) for dsn in dataset_names]))


    for dataset in datasets:
        train_rows = [r for r in content['$$Datasets'].tolist() if dataset in r]
        train = content[~content['$$Datasets'].isin(train_rows)]
        test = content[content['$$Datasets'].isin(train_rows)]

        del train['$$Datasets']
        del test['$$Datasets']

        assert(len(train) + len(test) == len(content)), "Something is wrong"
        temp = [get_prediction_error(train, test) for _ in xrange(20)]
        print
        obj1 = [t[0] for t in temp]
        obj2 = [t[1] for t in temp]
        print dataset, np.median(obj1), (np.percentile(obj1, 75) - np.percentile(obj1, 25)),
        print np.median(obj2), (np.percentile(obj2, 75) - np.percentile(obj2, 25))


if __name__ == "__main__":
    # getn_way("./Data/scalar_feature_model.csv")
    getn_way("./Data/scalar_se.csv")
