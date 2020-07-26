# Есть граф. Определить количество компонент связности. Определить, есть ли циклы

# Нужно проверить already visited вершину из данной вершины и проверка если она в стеке может не сработать
# сохранять посещённые для текущего узла

# проверить компоненты несвязанные
# graph_vertices_visited


def check_has_graph_cycles(graph):
  component_counter = 0
  has_graph_cycles = False
  path_travelled = []  # stack
  graph_vertices_unvisited = {i for i in range(len(graph))}

  while graph_vertices_unvisited:
    component_counter += 1

    first_vertice = graph_vertices_unvisited.pop()
    chosen_neighbour_index = 0
    path_travelled.append([first_vertice, chosen_neighbour_index])

    while path_travelled:
      [vertice, chosen_neighbour_index] = path_travelled[-1]
      neighbours = graph[vertice]

      if chosen_neighbour_index < len(neighbours):
        next_vertice = neighbours[chosen_neighbour_index]
        path_travelled[-1][1] += 1  # increment chosen neighbour index
        previous_vertice = path_travelled[-2][0] if len(path_travelled) > 1 else []
        if not (len(path_travelled) > 1 and next_vertice == previous_vertice):
          if next_vertice not in graph_vertices_unvisited:
            has_graph_cycles = True
            break
          else:
            graph_vertices_unvisited.remove(next_vertice)
            path_travelled.append([next_vertice, 0])
      else:
        path_travelled.pop()
    return component_counter, has_graph_cycles


# ======================== main


graph_with_cycle_v2 = [[1, 3], [0, 2], [1, 3], [0, 2]]
graph_without_cycle_v2 = [[3], [3], [3], [0, 1, 2]]

[components, cycles] = check_has_graph_cycles(graph_without_cycle_v2)

print("Graph has", components, "components. Graph has", "" if cycles else "no", "cycles")
