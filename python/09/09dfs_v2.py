graph_with_cycle_v2 = [[1, 3], [0, 2], [1, 3], [0, 2]]

def check_has_graph_cycles(graph):
  has_graph_cycles = False

  graph_vertices_unvisited = { i for i in range(len(graph)) }

  path_travelled = [] # stack

  # get_neighbours
  # is_visited
  # set_visited
  # get_from_stack
  # put_to_stack
  counter = 0
while graph_vertices_unvisited:
   counter += 1
  first_vertice = graph_vertices_unvisited.pop() 
  chosen_neighbour_index = 0
  path_travelled.append([first_vertice, chosen_neighbour_index])
  
  while path_travelled:
    vertice = path_travelled[-1][0]
    vertice_neighbours = graph[vertice]

    chosen_neighbour_index = path_travelled[-1][1]
    
    if chosen_neighbour_index < len(vertice_neighbours):
       next_vertice = vertice_neighbours[chosen_neighbour_index]
       path_travelled[-1][1] += 1 # increment chosen neighbour index
       previous_vertice = path_travelled[-2][0]
       if not (len(path_travelled) > 1 and next_vertice == previous_vertice):
           if next_vertice not in graph_vertices_unvisited:
                has_graph_cycles = True
                break
           else:
                graph_vertices_unvisited.remove(next_vertice)
                path_travelled.append([next_vertice, 0])
     else:
         path_travelled.pop()
   return counter, has_graph_cycles