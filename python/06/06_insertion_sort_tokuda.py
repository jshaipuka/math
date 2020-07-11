
import math

def TOKUDA(i): return math.floor(0.2*(9*(9/4)**(i-1)-4))

def insertion_sort(array, stepf):
  n = len(array)

  # 0.2*(9*(9/4)^(i-1)-4) < n
  # (9/4)^(i-1) < (5*n + 4)/9
  # i < log 9/4 ((5*n + 4)/9) + 1
  limit = math.floor(math.log((5 * n + 4)/9, 9/4) + 1)

  for i in range(limit, 0, -1):
    step = stepf(i)
    stepInsertionSort(array, i, step)
    print("Incrementing by", step, ". Sorted array:", array)
  return array


def stepInsertionSort(array, start, step):
  # from starting postion + "step" until array end do sorting with incrementing by "step"
  for position in range(start + step, len(array), step):
    currentvalue = array[position]

    # while current position is bigger than step and current value is less than value from current position - step
    while position >= step and array[position - step] > currentvalue:
      # swap and decrement position
      array[position], array[position - step] = array[position - step], array[position]
      position = position - step


test = [5, 1, 4, 5, 6, 7, 8, 2, 1, 11, 123, 2345, 4]

print(insertion_sort(test, TOKUDA))
