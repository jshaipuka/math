# 3. Использовать Дейкстру для поиска всех попарных расстояний
from math import inf
import heapq

def spf(graph, start, end):
  distance = {}
  unvisited = set()
  min_distance = [(0,start)]

  for node in graph.keys():
    distance[node] = inf if node != start else 0
    unvisited.add(node)
  
  while len(unvisited):
    current_distance, node = heapq.heappop(min_distance)

    if node == end: break

    if node in unvisited:
      unvisited.remove(node)

    for neighbour in graph[node].keys():
      alt = current_distance + graph[node][neighbour]
      if alt < distance[neighbour]:
        distance[neighbour] = alt
        heapq.heappush(min_distance, (alt, neighbour))

  return distance

def all_spf(graph):
  for from_node in graph.keys():
    paths = spf(graph, from_node, None)
    for to_node in paths:
      if from_node != to_node:
        print(from_node, '=>', to_node, ':', paths[to_node])



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

all_spf(graph)
