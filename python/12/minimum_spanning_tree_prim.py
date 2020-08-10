from math import inf

def min_node(unvisited, distance):
  min = None
  for node in unvisited:
    min = (node, distance[node]) if min is None or (distance[node] < min[1]) else min
  return min[0]

def mst(graph, start):
  distance = {}
  path = {}
  unvisited = set()

  for node in graph.keys():
    distance[node] = inf if node != start else 0
    path[node] = -1
    unvisited.add(node)
  
  while len(unvisited):
    node = min_node(unvisited, distance)

    unvisited.remove(node)

    for neighbour in graph[node].keys():
      if neighbour in unvisited:
        alt = graph[node][neighbour]
        if alt < distance[neighbour]:
          distance[neighbour] = alt
          path[neighbour] = node

  return (path, distance)

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

start = 'A'

result = mst(graph, start)
total_mst = sum(result[1].values())


print("Minimum spanning tree is", total_mst, ". Path: ", result[0])
# Minimum spanning tree is 15 . Path:  {'A': -1, 'B': 'D', 'C': 'E', 'D': 'A', 'E': 'F', 'F': 'D', 'G': 'B', 'H': 'F'}