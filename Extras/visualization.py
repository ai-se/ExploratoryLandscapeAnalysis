from __future__ import division
import pandas as pd
import os
import random

from sklearn.metrics import jaccard_similarity_score


def distance(lista, listb):
    return len(lista) - jaccard_similarity_score(lista, listb, normalize=False)


def calculate_distance_matrix(independents):
    distances = [[-1 for _ in xrange(len(independents))] for _ in xrange(len(independents))]
    for i in xrange(len(independents)):
        for j in xrange(len(independents)):
            if i == j:
                distances[i][j] = 0
            elif distances[i][j] == -1:
                distances[i][j] = distance(independents.iloc[i], independents.iloc[j])
                distances[j][i] = distances[i][j]
    return distances


def return_3d_list(filename):
    contents = pd.read_csv(filename)
    independent_columns = [c for c in contents.columns if "$<" not in c]
    independents = contents[independent_columns]
    dependent_column = [c for c in contents.columns if "$<" in c][-1]
    min_val_dependent = min(contents[dependent_column])
    max_val_dependent = max(contents[dependent_column])
    dependents = [(c - min_val_dependent)/(max_val_dependent - min_val_dependent) for c in contents[dependent_column]]

    random_index = random.randint(0, len(independents))
    random_indep = independents.iloc[random_index]

    t_east_indep_index = sorted([[distance(random_indep.tolist(), independents.iloc[i].tolist()), i] for i in xrange(len(independents))], key=lambda x: x[0])
    east_indep_index = t_east_indep_index[-1][-1]
    east_indep = independents.iloc[east_indep_index]

    t_west_indep_index = sorted([[distance(east_indep.tolist(), independents.iloc[i].tolist()), i] for i in xrange(len(independents))], key=lambda x: x[0])
    west_indep_index = t_west_indep_index[-1][-1]
    west_indep = independents.iloc[west_indep_index]

    print random_index, east_indep_index, west_indep_index

    c = distance(east_indep, west_indep)

    def projection(point):
        a = distance(east_indep, point)
        b = distance(west_indep, point)
        x = ((a**2 + c**2 - b**2)/(2*c))**0.5
        y = (a**2 - x**2)**0.5
        return [x, y]

    threed_points = []
    for i in xrange(len(independents)):
        x,y = projection(independents.iloc[i])
        threed_points.append([x, y, dependents[i]])

    # import pdb
    # pdb.set_trace()
    return threed_points


def draw_3d(name, points):
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    import random

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    zs = [p[2] for p in points]
    ax.scatter(xs, ys, zs, c='r', marker='o')

    plt.savefig("./visual_figures/" + name + ".png")
    plt.cla()

if __name__ == "__main__":
    filenames = ["../FeatureModels/" + f for f in os.listdir("../FeatureModels") if ".csv" in f]
    for file in filenames:
        if "AJStats" in file: continue
        print file
        import sys
        sys.stdout.flush()
        name = file.split('/')[-1]
        points = return_3d_list(file)
        draw_3d(name, points)