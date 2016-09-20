from __future__ import division
from random import shuffle
import pandas as pd
import numpy as np

points = [(4*x)**0.5 for x in xrange(1000)]
shuffle(points)
random_points = points[:100]

mean_distance = np.mean(distance_list)
mean_fitness = np.mean(dependent_values)
std_distance = np.std(distance_list)
std_fitness = np.std(dependent_values)

measure = 0
for i in xrange(n):
    measure += (distance_list[i] - mean_distance) * (dependent_values[i] - mean_fitness)
measure /= (n * std_distance * std_fitness)
print measure
