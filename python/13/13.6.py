# Даны несколько точек на плоскости, некоторые из которых соединены отрезками. Множество точек называется связанным, если из любой его точки можно перейти в любую точку, перемещаясь только по отрезкам (переходить с отрезка на отрезок возможно только в точках исходного множества). Можно за определенную плату добавлять новые отрезки (стоимость добавления равна длине добавляемого отрезка). Требуется за минимальную стоимость сделать данное множество связанным.


def solve(input):
  lines = [s for s in input.splitlines() if s]

  n = int(lines.pop(0))
  graph = createGraph(cities, lines)

  cities, avia_flights, nights_left, start_city, end_city = map(int, lines.pop(0).split())

# ============= main
input = '''
3
1 1
1 2
10 1
1
2 1
'''

solve(input)