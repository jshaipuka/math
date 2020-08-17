#  Дописать задачу с подстановками
# Подстановка σ задана двумя массивами a[1..n] и b[1..n] состоящими из всех различных чисел от 1 до n и такими, что b[i]=σ(a[i]) для каждого i=1,…,n (например, a=[2,3,1], b=[1,3,2] кодирует транспозицию (1,2)). Придумайте алгоритм, определяющий, содержит ли σ цикл длины k. Ваш алгоритм может изменять исходные массивы, но должен справляться с задачей за O(n^2) операций с использованием O(1) дополнительной памяти (оценивая эти две асимптотики, можете считать k константой).


# Assumption: cycle of 1 is ignored.
def solve(A, B):
  print('Solving', A, B)

  n = len(A)
  
  if n > 1: # ignore empty array. Also ignore array of 1, because ic contains a cycle of 1
    for i in range(n):
      ai = A[i]
      bi = B[i]

      # cycle of 1
      if ai == bi: continue

      b_next = B[A.index(bi)]
      while b_next != bi:
        if b_next == ai: return True
        b_next = B[A.index(b_next)]

  return False

# ======== main
test1 = [2, 3, 1], [1, 3, 2] # cycle
test2 = [1, 2, 3, 4, 5, 6], [5, 1, 6, 4, 2, 3]  # cycle
test3 = [1, 2], [2, 2] # no cycle


result = solve(*test1)
print('result', result)
