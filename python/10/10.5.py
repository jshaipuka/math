# Подстановка σ задана двумя массивами a[1..n] и b[1..n] состоящими из всех различных чисел от 1 до n и такими, что b[i]=σ(a[i]) для каждого i=1,…,n (например, a=[2,3,1], b=[1,3,2] кодирует транспозицию (1,2)). Придумайте алгоритм, определяющий, содержит ли σ цикл длины k. Ваш алгоритм может изменять исходные массивы, но должен справляться с задачей за O(n^2) операций с использованием O(1) дополнительной памяти (оценивая эти две асимптотики, можете считать k константой).

# Notes
# Подстановка = перестановка = permutation
# insertion, selectin, quick sort are O(n^2) time wih O(1) memory
# if a[i] = b[i] it's a cycle of k = 1

def sort(arr):
  for i in range(1, len(arr)):
    previousPermutation = arr[i - 1]
    nextPermutationDigit = previousPermutation[1]

    for j in range(i, len(arr)):
      if arr[j][0] == nextPermutationDigit:
        arr[i], arr[j] = arr[j], arr[i]
        break

  return arr

def solve(a, b):
  has_cycles = False

  if len(a) > 1:
    # tranform array A into array of permutations
    for i in range(len(a)):
      ai = a[i]
      bi = b[i]

      if ai == bi:
        has_cycles = True
        return has_cycles
      else:
        a[i] = f"{ai}{bi}"

    [first, *_, last] = sort(a)
    if first[0] == last[1]:
      has_cycles = True

  return has_cycles
      


#======================== main

test1 = {
  'a': [2,3,1],
  'b': [1,3,2] 
}

test2 = {
  'a': [1,3,4,6,7,8],
  'b': [4,7,6,8,1,3] 
}

test3 = {
  'a': [2, 4, 1],
  'b': [1, 3, 4] 
}

result = solve(**test2)

print('Permutations have', '' if result else 'no' , 'cycles')