# ещё вариант зранить 2 массива - на каждый уровень дерева.
# высота дерево = кол-во уровней
# можно раскрасить цвета


def find_min_steps_for_knight(start_coordinate, finish_coordinate, board_size):
  move_queue = [(start_coordinate[0], start_coordinate[1], 0)] # x, y, distance

  movements_x_y = [(2, 1), (-2, 1), (1, 2), (-1, 2),  (2, -1), (-2, -1), (1, -2), (-1, -2)]

  board_cells_visited = [[False] * board_size]]
  # board_cells_visited = [[False for i in range(board_size)] for j in range(board_size)] 
  board_cells_visited[start_coordinate[0]][start_coordinate[1]] = True # initial position 

  is_within_bounds = lambda coordinate, lower_bound, upper_bound: coordinate > lower_bound and coordinate < upper_bound

  while move_queue: # while queue is not empty
    first_in_queue = move_queue.pop(0)
    x = first_in_queue[0]
    y = first_in_queue[1]
    distance_so_far = first_in_queue[2]

    if x, y == finish_coordinate:
      # reached last cell. Should return stepsCount / distance
      return distance_so_far
    else:
      for move in movements_x_y:
        next_move_x = x + move[0]
        next_move_y = y + move[1]

        # is move possible
        is_move_valid = is_within_bounds(next_move_x, 0, board_size) and is_within_bounds(next_move_y, 0, board_size)
        is_move_valid_and_not_visited = is_move_valid and board_cells_visited[next_move_x][next_move_y] == False

        if is_move_valid_and_not_visited:
          print('From step', distance_so_far, 'we can move to', move)
          # if move is posssible add to move queue and increse distance travelled
          board_cells_visited[next_move_x][next_move_y] = True
          next_move = (next_move_x, next_move_y, distance_so_far + 1)
          move_queue.append(next_move)

#======================== main

board_size = 8
knight_first_cell = (0,0)
knight_last_cell = (board_size - 1, board_size - 1)

result = find_min_steps_for_knight(knight_first_cell, knight_last_cell, board_size)
print("Minimum steps for the knight from cell", knight_first_cell, "to cell", knight_last_cell, " on a", board_size , " x ", board_size, " board is", result)