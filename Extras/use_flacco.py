from __future__ import division
import pyRserve
from os import listdir
import pandas as pd
from random import shuffle


def df_to_list_str(df):
    columns = df.columns.tolist()
    list = []
    for column in columns:
        list.extend(df[column].tolist())
    result_str = ""
    for i, l in enumerate(list):
        result_str += str(l)
        if i<len(list)-1: result_str += ","
    return result_str


def get_ela_features(independent, dependent):
    # rcmd = pyRserve.connect(host='localhost', port=6311)
    # print(rcmd.eval('rnorm(100)'))
    features = {}
    i_ncols = len(independent.columns)
    str_indep = "matrix(c(" + df_to_list_str(independent) + "), ncol=" + str(i_ncols) + ")"
    str_dep = "matrix(c(" + df_to_list_str(dependent) + "), ncol=" + str(1) + ")"

    assert(len(independent) == len(dependent)), "sanity check failed"
    conn = pyRserve.connect(host='localhost', port=6311)
    conn.voidEval("library('flacco')")
    conn.voidEval("X <- " + str_indep)
    conn.voidEval("y<- " + str_dep)
    conn.voidEval("feat.object = createFeatureObject(X = X, y = y, blocks = 3)")
    fs1 = conn.r("calculateFeatureSet(feat.object, set = 'ela_distr')")
    for name, value in zip(fs1.keys, fs1.values):
        features[name] = value
    # fs2 = conn.r("calculateFeatureSet(feat.object, set = 'ela_level')")
    # for name, value in zip(fs2.keys, fs2.values):
    #     features[name] = value
    # fs3 = conn.r("calculateFeatureSet(feat.object, set = 'ela_meta')")
    # for name, value in zip(fs3.keys, fs3.values):
    #     features[name] = value
    # fs4 = conn.r("calculateFeatureSet(feat.object, set = 'cm_grad')")
    # for name, value in zip(fs4.keys, fs4.values):
    #     features[name] = value
    return features

if __name__ == "__main__":

    files = ["../FeatureModels/" + f for f in listdir("../FeatureModels") if ".csv" in f]
    for filename in ["../FeatureModels/BerkeleyDB.csv"]:
        contents = pd.read_csv(filename)
        independent_columns = [c for c in contents.columns if "$<" not in c]
        dependent_column = [c for c in contents.columns if "$<" in c]
        independents = contents[independent_columns]
        raw_dependents = contents[dependent_column]
        dependents = (raw_dependents - raw_dependents.mean()) / (raw_dependents.max() - raw_dependents.min())

        indexes = range(len(contents))
        shuffle(indexes)

        n = 100#min(n, int(len(contents) * 0.1))
        samples = indexes[:n]
        independent_values = independents[independents.index.isin(samples)]

        dependent_values = dependents[dependents.index.isin(samples)]
        print filename
        print get_ela_features(independent_values, dependent_values)
        exit()