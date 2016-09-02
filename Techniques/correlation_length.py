from __future__ import division
from random import choice, randint
import pandas as pd

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
        start_node = choice(dataset[start_node].neighbors)
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

# def

if __name__ == "__main__":
    graph = generate_graph("../FeatureModels/Apache.csv")
    rp1 = random_walk(graph, 10)
    fitness = [graph[c].dependent_value for c in rp1]
    norm_fitness = [(f-min(fitness))/(max(fitness) - min(fitness)) for f in fitness]
    print fitness
    print norm_fitness
