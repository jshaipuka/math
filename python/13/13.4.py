# В ориентированном взвешенном графе вершины пронумерованы числами от 1 до n. Если i < j, то существует ребро из вершины i в вершину j, вес которого определяется по формуле wt(i,j)=(179i+719j) mod 1000 - 500. Определите вес кратчайшего пути, ведущего из вершины 1 в вершину n.

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
  nodes = range(len(graph))

  dist = init_sssp(nodes, start)

  for _ in range(len(nodes)):
    for node in nodes:
      for neighbour in range(len(graph[node])):
        if graph[node][neighbour] != 0:
          relax(dist, node, neighbour, graph[node][neighbour])

  return dist[end]

def create_graph(n):
  matrix = [ [0] * n for _ in range(n)]
  calculate_weight = lambda nodei, nodej: (179 * nodei + 719 * nodej) % 1000 - 500

  for nodei in range(n):
    for nodej in range(n):
      matrix[nodei][nodej] = calculate_weight(nodei + 1, nodej + 1) if nodei < nodej else inf
  return matrix

def solve(n):
  graph = create_graph(n)
  return bellman_ford(graph, 0, n - 1)


# ========== main

# nodei, nodej  are nodes
# if nodei < nodej then it has edge with weight calculate_weight
# Find spf from 1 to N.


# V 1 sekundu na boljshih znachinjah N ne ulozhitsja. Heap?
print('Result', solve(3))