from __future__ import division
from random import choice, randint
import pandas as pd
import numpy as np

class Node():
    def __init__(self, node_id, independent, dependent):
        self.node_id = node_id
        self.independent_value = independent
        self.dependent_value = dependent
        self.neighbors = []

    def add_neighbors(self, neighbors):
        self.neighbors = neighbors

    def random_neighbor(self):
        return choice(self.neighbors)


def random_walk(dataset, length_of_walk):
    """ This function would accept a graph of the dataset as an input
    and return a path of the length specified """
    number_of_nodes = len(dataset)
    start_node = randint(0, number_of_nodes)
    walk = [start_node]
    for _ in xrange(length_of_walk):
        try:
            start_node = choice(dataset[start_node].neighbors)
        except:
            print dataset[start_node].neighbors, start_node
        walk.append(dataset[start_node].node_id)
    return walk


def generate_graph(filename):
    Nodes = []
    contents = pd.read_csv(filename)
    independent_columns = [c for c in contents.columns if "$<" not in c]
    dependent_column = [c for c in contents.columns if "$<" in c][-1]
    independents = contents[independent_columns]
    dependents = contents[dependent_column]

    from scipy.spatial.distance import pdist, squareform
    distance_matrix = squareform(pdist(independents, 'euclidean'))
    for i in range(len(contents)):
        temp_node = Node(i, independents.iloc[i], dependents.iloc[i])
        neighbor_distances = distance_matrix[i].tolist()

        # replace 0 with a high value
        neighbor_distances = [1e20 if nd == 0 else nd for nd in neighbor_distances]

        # Indexes of minimum value
        neighbor = [i for i,c in enumerate(neighbor_distances) if c==min(neighbor_distances)]

        temp_node.add_neighbors(neighbor)
        Nodes.append(temp_node)
    assert(len(Nodes) == len(contents)), "Sanity check failed"
    return Nodes


def get_correlation_length(filename, m=20, s=1):
    graph = generate_graph(filename)
    rp1 = random_walk(graph, m)
    fitness = [graph[c].dependent_value for c in rp1]
    # print fitness,
    variance = np.var(fitness)
    mean_f = np.mean(fitness)
    temp_correlation_length = 0
    for i in xrange(m-1):
        temp_correlation_length += (fitness[i] - mean_f)*(fitness[i+1] - mean_f)
    r_s = temp_correlation_length/(variance * (m-s))
    correlation_length = -1/np.log(abs(r_s))
    return round(correlation_length, 3)

if __name__ == "__main__":
    for m in xrange(10, 25):
        print m, np.mean([get_correlation_length("../FeatureModels/Apache.csv", m=m) for _ in xrange(10)])
