from __future__ import division
from random import random
import pandas as pd
import os

def assign_weights(number):
    rand_number = [random() for _ in xrange(number)]
    r = sum(rand_number)
    temp = [no/float(r) for no in rand_number]
    assert(int(round(sum(temp),0)) == 1),"Something's wrong"
    return temp


def get_scalar_obj(objectives):
    return_objectives = []
    number_of_objectives = len(objectives[0])
    weights = assign_weights(number_of_objectives)
    for objective in objectives:
        temp_sum = 0
        for weight, o in zip(weights, objective):
            temp_sum += weight * o
        return_objectives.append(temp_sum)
    return return_objectives


def get_columns(filename):
    e_name = filename.split("/")[-1].split(".")[0]
    content = pd.read_csv(filename)
    columns = content.columns
    # For FeatureModels
    # independent_columns = [c for c in columns if "$<" not in c]
    # dependent_columns = [c for c in columns if "$<" in c]

    independent_columns = [c for c in columns if ">>" not in c]
    dependent_columns = [c for c in columns if ">>" in c]

    i_content = content[independent_columns]
    d_content = content[dependent_columns]
    d_content_list = [d_content.iloc[i].tolist() for i in xrange(len(d_content)) ]
    for i in xrange(50):
        obj = get_scalar_obj(d_content_list)
        df = pd.DataFrame({'$<obj': obj})
        df = df.join(i_content)
        df.to_csv("../scalar_dataset/" + e_name + "_" + str(i) + ".csv", index=False)

if __name__ == "__main__":
    # files = ["../MultiFeatureModels/" + f for f in os.listdir("../MultiFeatureModels/") if ".csv" in f]
    files = ["../SEModels/" + f for f in os.listdir("../SEModels/") if ".txt" in f]
    for file in files:
        get_columns(file)
