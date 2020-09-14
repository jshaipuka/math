graph_with_cycle_v2 = [[1, 3], [0, 2], [1, 3], [0, 2]]

def check_has_graph_cycles(graph):
  has_graph_cycles = False

  graph_vertices_visited = set()

  path_travelled = [] # stack

  # get_neighbours
  # is_visited
  # set_visited
  # get_from_stack
  # put_to_stack

  first_vertice = 0 
  first_vertice_neighbours = graph[first_vertice]
  chosen_neighbour_index = 0
  path_travelled.append([first_vertice, chosen_neighbour_index])
  graph_vertices_visited.append(first_vertice)

  while path_travelled:
    vertice = path_travelled[-1][0]
    vertice_neighbours = graph[vertice]

    chosen_neighbour_index = path_travelled[-1][1]
    
    if chosen_neighbour_index < len(vertice_neighbours):
       next_vertice = vertice_neighbours[chosen_neighbour_index]
       path_travelled[-1][1] += 1 # increment chosen neighbour index
       previous_vertice = path_travelled[-2][0]
       if not (len(path_travelled) > 1 and next_vertice == previous_vertice):
           if next_vertice in graph_vertices_visited:
                has_graph_cycles = True
                break
           else:
                graph_vertices_visited.add(next_vertice)
                path_travelled.append([next_vertice, 0])
     else:
         path_travelled.pop()
   return has_graph_cycles


if next_vertice in graph_vertices_visited

			 path_travelled.append((neighbour, next_chosen_neighbour_index))
    is_visited = neighbour in graph_vertices_visited
				if is_visited:
						path_travelled.pop()
				else:
						graph_vertices_visited.add(neighbour)
      neighbour_neighbours = graph[neighbour]

							
