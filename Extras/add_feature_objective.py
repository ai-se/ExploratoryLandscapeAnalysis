from __future__ import division

def new_objective(decision):
    return sum(decision)


def wrapper(filename):
    e_filename = filename.split("/")[-1].split(".")[0]
    import pandas as pd
    content = pd.read_csv(filename)
    columns = content.columns
    indep = [c for c in content if "$<" not in c]
    dep = [c for c in content if "$<" in c]
    c_indep = content[indep]
    new_deps = []
    for i in xrange(len(c_indep)):
        new_deps.append(new_objective(c_indep.iloc[i]))
    df = pd.DataFrame({'$<obj2': new_deps})
    content = content.join(df)
    content.to_csv("../MultiFeatureModels/" + e_filename + ".csv", index=False)

if __name__ == "__main__":
    import os
    files = ["../FeatureModels/" + file for file in os.listdir("../FeatureModels/") if ".csv" in file]
    for file in files:
        print file
        wrapper(file)
