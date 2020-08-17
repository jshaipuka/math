# Bellman-Ford
from math import inf

def init_sssp(nodes, start):
  dist = {}

  for node in nodes:
    dist[node] = inf if node != start else 0

  return dist

def relax(dist, u, v, weight):
  new_dist = dist[u] + weight
  if new_dist < dist[v]:
    dist[v] = new_dist

def bellman_ford(graph, start, end):
  nodes = [*graph.keys()]

  dist = init_sssp(nodes, start)

  for _ in range(len(nodes)):
    for node in nodes:
      for neighbour in graph[node].keys():
        if graph[node][neighbour] != 0:
          relax(dist, node, neighbour, graph[node][neighbour])

  print('dist', dist)
  return dist[end]

# ==============
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

graph2 = {
    'A': {'B': 3, 'G': 10, 'F': 4},
    'B': {'C': 2, 'G': 6},
    'C': {},
    'D': {'C': -5},
    'E': {'C': -3, 'D': 1},
    'F': {'G': 8, 'E': 3},
    'G': {'C': -7, 'E': -5}
}

print('GRAPH_1: from G to H', bellman_ford(graph, 'G', 'H'))
print('GRAPH_2: from A to C', bellman_ford(graph2, 'A', 'C'))

