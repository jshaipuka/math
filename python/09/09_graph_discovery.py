# Есть граф. Определить количество компонент связности. Определить, есть ли циклы


def check_has_graph_cycles(graph):
  has_graph_cycles = False

  graph_vertices_visited = set()

  for i in range(len(graph)):
    for j in range(len(graph)):
      if graph[i][j] == 1:
        if j not in graph_vertices_visited:
          graph_vertices_visited.add(j)
        else:
          has_graph_cycles = True

  return ("unknown number of", has_graph_cycles)


#======================== main

  # graph_vertices_visited = [[False for i in range(board_size)] for j in range(board_size)] 

# via adjacency matrices
graph_with_cycle = [[0,1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1,0]]
graph_without_cycle = [[0,0,0,1], [0,0,0,1], [0,0,0,1], [1,1,1,0]]

result = check_has_graph_cycles(graph_with_cycle)

print("Graph has", result[0], "components. Graph has", result[1], "cycles")