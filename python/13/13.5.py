# Профессору Форду необходимо попасть на международную конференцию. Он хочет потратить на дорогу наименьшее количество денег, поэтому решил, что будет путешествовать исключительно ночными авиарейсами (чтобы не тратиться на ночевку в отелях), а днем будет осматривать достопримечательности тех городов, через которые он будет проезжать транзитом. Он внимательно изучил расписание авиаперелетов и составил набор подходящих авиарейсов, выяснив, что перелеты на выбранных направлениях совершаются каждую ночь и за одну ночь он не сможет совершить два перелета.

# Теперь профессор хочет найти путь наименьшей стоимости, учитывая что до конференции осталось K ночей (то есть профессор может совершить не более K перелетов).

# Входные данные
# В первой строке находятся числа N (количество городов), M (количество авиарейсов), K (количество оставшихся ночей), S (номер города, в котором живет профессор), F (номер города, в котором проводится конференция).

# Ограничения: 2≤N≤100, 1≤M≤105, 1≤K≤100, 1≤S≤N, 1≤F≤N.

# Далее идет M строк, задающих расписание авиарейсов. i-я строка содержит три натуральных числа: Si, Fi и Pi, где Si - номер города, из которого вылетает i-й рейс, Fi - номер го-рода, в который прилетает i-й рейс, Pi - стоимость перелета i-м рейсом. 1≤Si≤N, 1≤Fi≤N, 1≤Pi≤106.

# Выходные данные
# Выведите одно число - минимальную стоимость пути, подходящего для профессора. Если профессор не сможет за K ночей добраться до конференции, выведите число -1.

from math import inf

def createGraph(n, input):
  matrix = [ [0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      matrix[i][j] = inf
  
  for line in input:
    i, j, cost = map(int, line.split())
    matrix[i - 1][j - 1] = cost

  return matrix

def init_sssp(nodes, start):
  dist = {}

  for node in nodes:
    dist[node] = inf if node != start else 0

  return dist

def relax(dist, u, v, weight):
  new_dist = dist[u] + weight
  if new_dist < dist[v]:
    dist[v] = new_dist

def bellman_ford(graph, start, end, max_hops):
  nodes = range(len(graph))

  dist = init_sssp(nodes, start)
  path = {start: None}

  for _ in range(max_hops):
    dist1 = dist.copy()
    for node in nodes:
      for neighbour in range(len(graph[node])):
        if graph[node][neighbour] != 0:
          new_dist = dist[node] + graph[node][neighbour]
          if new_dist < dist[neighbour]:
            dist1[neighbour] = new_dist
            path[neighbour] = node
    dist = dist1.copy()

  return dist[end]

def solve(input):
  lines = [s for s in input.splitlines() if s]
  cities, avia_flights, nights_left, start_city, end_city = map(int, lines.pop(0).split())
  graph = createGraph(cities, lines)

  print(graph)

  total_flight_cost = bellman_ford(graph, start_city - 1, end_city - 1, nights_left)

  print('total_flight_cost', total_flight_cost)

# ============= main
input = '''
4 5 2 1 4
1 2 1
2 3 1
3 4 1
1 3 3
1 4 5
'''

solve(input)