import functools 

def has_cycle(graph, node):
  has_cycles = False
  path = [[node, set(graph[node].keys())]]
  visited = {node}
  
  while path:
    last_node = path[-1]

    if last_node[1]:
      next_node = last_node[1].pop()
      if next_node in visited:
        has_cycles = True
        break
      else:
        visited.add(next_node)
        path.append([next_node, set(graph[next_node].keys())])
        try:
          path[-1][1].remove(last_node[0]) # remove from path to not comeback
        except Exception:
          print(graph, last_node[0], next_node, node)
          raise "Tooo bad"
    else:
      path.pop()
  
  return has_cycles


def mst(graph):
  vertices = dict()
  edges = [] #отсортированный список
  graph_copy = {el: graph[el].copy() for el in graph}

  for node in graph.keys():
    for neighbour in graph_copy[node].keys():
      edges.append((graph[node][neighbour], node, neighbour))
      graph_copy[neighbour].pop(node)
    graph_copy.pop(node)

  edges.sort()
  counter = 0

  for edge in edges:
    if counter == len(graph) - 1:
      break
    vertices.setdefault(edge[1], dict())
    vertices.setdefault(edge[2], dict())
    vertices[edge[1]][edge[2]] = edge[0]
    vertices[edge[2]][edge[1]] = edge[0]
    # проверка на цикл
    
    if has_cycle(vertices, edge[1]):
      vertices[edge[1]].pop(edge[2])
      vertices[edge[2]].pop(edge[1])

  return vertices, functools.reduce(lambda a,b: a+b, [vertices[el][el_2] for el in vertices for el_2 in vertices[el]])//2

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

print(*mst(graph), sep = "\nlength = ")

