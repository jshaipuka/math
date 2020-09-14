# Дан массив A[1:n] вещественных чисел, отсортированный по возрастанию, а также числа p, q, r. Предложите алгоритм, строящий массив B[1:n], состоящий из чисел px^2+qx+r, где x∈A, также отсортированный по возрастанию. Ограничение по времени — O(n), по дополнительной памяти — O(n)

def merge(leftArray, rightArray):
  leftIndex, rightIndex = 0, 0
  leftArrayLength = len(leftArray)
  rightArrayLength = len(rightArray)
  
  sorted = []
  
  while leftIndex < leftArrayLength or rightIndex < rightArrayLength:
    if rightIndex == rightArrayLength or (leftIndex < leftArrayLength and leftArray[leftIndex] <= rightArray[rightIndex]):
      sorted.append(leftArray[leftIndex])
      leftIndex = leftIndex + 1
    else:
      sorted.append(rightArray[rightIndex])
      rightIndex = rightIndex + 1

  return sorted

def solve_B(params, forward = True):
  [ A, p, q, r ] = params
  B = []

  start = 0 if forward else len(A) - 1
  stop = len(A) if forward else -1
  step = 1 if forward else -1
  
  for i in range(start, stop, step):
    x = A[i]
    y = p * x**2 + q * x + r
    B.append(y)
  return B

def solve_B_quadratic(params, forward = True, x0 = None):
  [ A, p, q, r ] = params
  B = []

  start = 0 if forward else len(A) - 1
  stop = len(A) if forward else -1
  step = 1 if forward else -1

  index_of_closest_x0 = -1

  for i in range(start, stop, step):
    x = A[i]
    y = p * x**2 + q * x + r
    B.append(y)

    if x < x0 and forward:
      index_of_closest_x0 = i # found where x0 is in array

  if index_of_closest_x0 == -1 or A[len(A) - 1] < x0: # not found or all array items are smaller than x0
    if p < 0:
      if index_of_closest_x0 == -1: # is on the left
        return B[::-1]
      else:
        return B
    else:
      if index_of_closest_x0 == -1: # is on the left
        return B
      else:
        return B[::-1]
  else:
    if p > 0:
      return merge(B[:index_of_closest_x0 + 1][::-1], B[index_of_closest_x0 + 1:])
    else:
      return merge(B[:index_of_closest_x0 + 1], B[index_of_closest_x0 + 1:][::-1])

def solve(params):
  [ A, p, q, r ] = params
  
  if p == 0 and q == 0 and r ==0:
    return [0 for _ in range(len(A))]
  if p == 0 and q == 0:
    return [r for _ in range(len(A))]
  elif p == 0:
    if q > 0:
      #solve forward
      return solve_B(params)
    else:
      #solve reverse
      return solve_B(params, False)
  else:
    x0 = -q / (2 * p)
    return solve_B_quadratic(params, True, x0)


A = [-100, -3, -2, -0.5, 1, 2]
p = -1
q = 15
r = 0

test = [A, p, q, r]

print(solve(test))