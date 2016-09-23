from __future__ import division
import sys, os, inspect

parentdir = os.path.realpath(
    os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "../")))
if parentdir not in sys.path:
    sys.path.insert(0, parentdir)

import pandas as pd
import numpy as np


distance_matrix = []

def euclidean_distance(list1, list2):
    assert(len(list1) == len(list2)), "The points don't have the same dimension"
    distance = sum([(i - j) ** 2 for i, j in zip(list1, list2)]) ** 0.5
    assert(distance >= 0), "Distance can't be less than 0"
    return distance

def get_c_r(content, r):
    global distance_matrix
    lines = len(content)
    sum_value = 0
    for i in xrange(lines):
        for j in xrange(i+1, lines):
            if distance_matrix[i][j] <= r:
                sum_value += 1
    print '#',
    sys.stdout.flush()
    c_r = (2/(lines * (lines-1))) * sum_value
    return np.log(c_r)


def highest_r():
    global distance_matrix
    max_value = -1e20
    for d in distance_matrix:
            max_value = max(max_value, max(d))
    return max_value

def generate_distance_matrix(content):
    lines = len(content)
    global distance_matrix
    for i in xrange(lines):
        temp = []
        for j in xrange(lines):
            temp.append(euclidean_distance(content.iloc[i], content.iloc[j]))
        distance_matrix.append(temp)

def generate_distance_matrix2(X):
    global distance_matrix
    from scipy.spatial.distance import pdist, squareform
    distance_matrix = squareform(pdist(X,'euclidean'))


def intrinsic_dimenstionality(cont):
    content = cont
    generate_distance_matrix2(content)
    number_of_dimensions = len(content.columns)
    print ">>> ", number_of_dimensions
    high_r = highest_r()
    values_r = [i * 0.05 * high_r for i in xrange(1, 20)]
    log_c_r = [get_c_r(content, r) for r in values_r]
    log_r = map(lambda x:np.log(x), values_r)
    slopes = []
    for i in xrange(len(log_r)-1):
        slopes.append((log_c_r[i+1]-log_c_r[i])/(log_r[i+1]-log_r[i]))
    slopes = [s for s in slopes if not np.isnan(s) and not np.isinf(s)]
    return np.mean(slopes)

if __name__ == "__main__":
    files = [
    "Apache_AllMeasurements",
    "BDBC_AllMeasurements",
    "BDBJ_AllMeasurements",
    "LLVM_AllMeasurements",
    "SQL_AllMeasurements",
    "X264_AllMeasurements"
    ]
    for file in files:
        print file,
        content = pd.read_csv("./data/" + file + ".csv")
        content = content.replace('Y', 1)
        content = content.replace('N', 0)
        indep = [c for c in content.columns if "$<" not in c]
        print len(indep),
        content = content[indep]
        generate_distance_matrix2(content)

        print intrinsic_dimenstionality(content)