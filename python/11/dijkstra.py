from math import inf

def min_node(unvisited, distance):
  min = None
  for node in unvisited:
    min = (node, distance[node]) if min is None or (distance[node] < min[1]) else min
  return min[0]

def spf(graph, start, end):
  distance = {}
  unvisited = set()

  for node in graph.keys():
    distance[node] = inf if node != start else 0
    unvisited.add(node)
  
  while len(unvisited):
    node = min_node(unvisited, distance)
  
    if node == end: break
    unvisited.remove(node)

    for neighbour in graph[node].keys():
      alt = distance[node] + graph[node][neighbour]
      distance[neighbour] = alt if alt < distance[neighbour] else distance[neighbour]

  print('distances', distance)
  return distance[end]

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
start = 'G'
end = 'H'

shortest_path = spf(graph, start, end)

print("Shortest path from ", start, " to ", end, " is ", shortest_path)
