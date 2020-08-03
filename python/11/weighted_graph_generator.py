#  генератор взвешенных графов для тестировани

import numpy as np
import random

def weighted_graph_as_matrix(n, only_positive=True):
  matrix = [ [0]*n for i in range(n)]

  randomize_start = 0 if only_positive else -10
  randomize_stop = 10

  for from_node_index in range(n):
    for to_node_index in range(n):
      matrix[from_node_index][to_node_index] = random.randrange(randomize_start, randomize_stop)
  return matrix

#======================== main

matrix = weighted_graph_as_matrix(n = 5, only_positive = True)

print('Adjacency matrix \n', np.matrix(matrix))