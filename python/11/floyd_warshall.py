from math import inf
import numpy as np
import heapq

def graph_as_matrix(graph):
  nodes = [*graph.keys()]
  n = len(nodes)
  matrix = [ [0]*n for i in range(n)]

  for from_node_index in range(n):
    for to_node_index in range(n):
      from_node = nodes[from_node_index]
      to_node = nodes[to_node_index]
      if from_node_index == to_node_index:
        matrix[from_node_index][to_node_index] = 0
      else:
        matrix[from_node_index][to_node_index] = graph[from_node][to_node] if to_node in graph[from_node] else inf
  return matrix



def sp(nodes, matrix, start, end):
  n = len(nodes)
  for k in range(n):
    for i in range(n):
      for j in range(n):
        old_path = matrix[i][j]
        new_path = matrix[k][j] + matrix[i][k]
        if new_path < old_path:
          matrix[i][j] = new_path
  
  return matrix
      

#======================== main

graph = {
    'A': {'G': 3, 'D': 3},
    'B': {'D': 1, 'E': 6, 'G': 2},
    'C': {'E': 2,'G': 5},
    'D': {'A': 3, 'B': 1, 'F': 4},
    'E': {'C': 2, 'B': 6, 'F': 1, 'H': 4},
    'F': {'D': 4, 'E': 1, 'H': 2},
    'G': {'A': 3, 'B': 2, 'C': 5},
    'H': {'E': 4, 'F': 2},
}

nodes = [*graph.keys()]
matrix = graph_as_matrix(graph)
start =  6 # 'G'
end = 7 # 'H'

print('Adjacency matrix \n', np.matrix(matrix))

shortest_path = sp(nodes, matrix, start, end)
print('Adjacency matrix \n', np.matrix(shortest_path))

print("Shortest path from ", nodes[start], " to ", nodes[end], " is ", shortest_path[start][end])
