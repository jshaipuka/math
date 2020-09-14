import math

def solve(maze, approximation_func):
  start = maze[0][0]
  finish = maze[len(maze) - 1][len(maze) - 1]

  

  print('not solved')


# esli i = 1, to eto prepjatstvie
maze = [
  [0, 1, 0, 0],
  [0, 0, 0, 0],
  [0, 1, 0, 0]
]

approximation_func = lambda a, b: math.sqrt(a**2 + b**2)

print(solve(maze, approximation_func))