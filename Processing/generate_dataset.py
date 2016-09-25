from __future__ import division
import os
import numpy as np
from intrinsicD import intrinsic_dimenstionality
import pandas as pd
from random import choice

features = [
    'ela_distr.skewness',
    'ela_distr.kurtosis',
    'ela_distr.number_of_peaks',
    'ela_distr.costs_fun_evals',
    'ela_distr.costs_runtime',
    'ela_meta.lin_simple.adj_r2',
    'ela_meta.lin_simple.intercept',
    'ela_meta.lin_simple.coef.min',
    'ela_meta.lin_simple.coef.max',
    'ela_meta.lin_simple.coef.max_by_min',
    'ela_meta.lin_w_interact.adj_r2',
    'ela_meta.quad_simple.adj_r2',
    'ela_meta.quad_simple.cond',
    'ela_meta.quad_w_interact.adj_r2',
    'ela_meta.costs_fun_evals',
    'ela_meta.costs_runtime',
    'nbc.nn_nb.sd_ratio',
    'nbc.nn_nb.mean_ratio',
    'nbc.nn_nb.cor',
    'nbc.dist_ratio.coeff_var',
    'nbc.nb_fitness.cor',
    'nbc.costs_fun_evals',
    'nbc.costs_runtime',
    'ic.h.max',
    'ic.eps.s',
    'ic.eps.max',
    'ic.eps.ratio',
    'ic.m0',
    'ic.costs_fun_evals',
    'ic.costs_runtime',
    'no_decisions',
]

def number_of_features_selected(content):
    rows = len(content)
    counts = []
    for i in xrange(rows):
        counts.append((content.iloc[i].tolist()).count(1))
    assert(len(content) == len(counts)), "something is wrong"
    return counts


def condese_datasets(result_dir, filename):
    print filename
    dataset_name = filename.split("/")[-1].split(".")[0]
    files = [result_dir + f for f in os.listdir(result_dir) if dataset_name in f]
    data = {}
    for f in features: data[f] = []
    for file in files:
        content = open(file).readlines()
        assert(len(content) == len(features)), "something is wrong"
        for i,c in enumerate(content):
            try:
                data[features[i]].append(float(c.strip()) )
            except: data[features[i]].append(c.strip())
    temp = [dataset_name]
    for f in features:
        try:
            temp.extend([round(np.median(data[f]), 3)])
        except:
            temp.extend([data[f][0]])

    content = pd.read_csv(filename)
    dec = []
    obj = []
    decision_id_list = []
    for _ in xrange(1):
        # indexes = range(len(content))
        # index_subsample =[choice(indexes) for _ in xrange(100)]
        dcolumns = [c for c in content.columns if "$<" not in c]
        ocolumns = [c for c in content.columns if "$<" in c]

        dcontent_subsample = content.sample(1000) if len(content) > 1000 else content.sample(len(content))
        # dcontent_subsample_norm = (dcontent_subsample - dcontent_subsample.min()) / (dcontent_subsample.max() - dcontent_subsample.min())
        dec.append(intrinsic_dimenstionality(dcontent_subsample[dcolumns]))

        ocontent = dcontent_subsample[ocolumns].reset_index()
        df = pd.DataFrame({'<$obj2': number_of_features_selected(dcontent_subsample[dcolumns])})
        ocontent = ocontent.join(df)
        ocontent = ocontent.drop('index', 1)
        onorm = (ocontent - ocontent.min()) / (ocontent.max() - ocontent.min() + 0.00001)
        obj.append(intrinsic_dimenstionality(onorm))

    return temp + [round(np.median(dec), 3), round(np.median(obj), 3)]

if __name__ == "__main__":
    csv_result = []

    name_entry = ['Datasets']
    for f in features:
        name_entry.extend([f + 'median'])
    name_entry += ['IDem_Decision', 'IDem_Objective']
    csv_result.append(name_entry)
    for name in os.listdir("../scalar_dataset/"):
        if ".csv" not in name: continue
        n = name.split(".")[0]
        csv_result.append(condese_datasets("../Result_scalar_models/", "../scalar_dataset/" + name))


    import csv

    with open("median_scores_feature_model.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(csv_result)
