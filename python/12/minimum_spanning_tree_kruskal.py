# Ne rabotaet

from math import inf

def min_edge(edges):
  min = None
  for node in edges.keys():
    min = (node, edges[node]) if min is None or (edges[node] < min[1]) else min
  return min[0]

def mst(graph):
  visited = set()
  visited_edges = set()
  edges = {}

  for node in graph.keys():
    for neighbour in graph[node].keys():
      edge = node + neighbour
      same_edge = neighbour + node

      if edge in edges or same_edge in edges:
        continue
      else:
        edges[edge] = graph[node][neighbour]
  
  while len(edges.keys()):
    edge = min_edge(edges)
    [node_from, node_to] = edge

    edges.pop(edge)

    # Does adding edge to result spanning tree create a cycle or not
    if node_from in visited and node_to in visited: 
      continue
    else:
      visited_edges.add(edge)
      if node_from not in visited:
        visited.add(node_from)
      if node_to not in visited:
        visited.add(node_to)
  
  print('result', visited) # result {'D', 'C', 'A', 'E', 'H', 'F', 'G', 'B'}
  print('result', visited_edges) # result {'AG', 'BD', 'BG', 'CE', 'FH', 'EF'}
  return visited_edges

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

result = mst(graph)