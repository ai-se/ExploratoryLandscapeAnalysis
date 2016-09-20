from __future__ import division
import os
import numpy as np

features = [
    'nbc.nn_nb.sd_ratio',
    'nbc.nn_nb.mean_ratio',
    'nbc.nn_nb.cor',
    'nbc.dist_ratio.coeff_var',
    'nbc.nb_fitness.cor',
    'nbc.costs_fun_evals',
    'nbc.costs_runtime',
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
]

def condese_datasets(result_dir, dataset_name):
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
            temp.extend([round(np.mean(data[f]), 3), round(np.std(data[f]), 3)])
        except:
            temp.extend([data[f][0], data[f][0]])
    return temp

if __name__ == "__main__":
    csv_result = []

    name_entry = []
    for f in features:
        name_entry.extend([f + 'mean', f + 'std'])
    csv_result.append(name_entry)
    for name in os.listdir("../FeatureModels/"):
        n = name.split(".")[0]
        csv_result.append(condese_datasets("../Result_FeatureModels/", n))
    print csv_result

import csv

with open("feature_models_stability_scores.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(csv_result)