# На уроке мы обсуждали задачу с сортировкой массива A, при оставлении на месте элементов, которые есть в массиве B. Попробуйте решить ее меньше чем за O(n^2) (считаем, что n >> m)

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

def merge_sort(array, b):
  if len(array) == 1:
    return array
  else:
    half = len(array) // 2
    return merge(merge_sort(array[:half]), merge_sort(array[half:]))


def sort(a, b):
  a_dont_touch_indexes = []
  
  for i in range(len(a)):
    found = b.index(a[i])
    if found:
      a_dont_touch_indexes.append(found)
  
  return merge_sort(a, a_dont_touch_indexes)
  
  
  

  



test1 = {
  'a': [2,3,1, 7, 8],
  'b': [1,3,2, 4] 
}

test2 = {
  'a': [2,3,1,],
  'b': [1,3,2,] 
}

result = sort(**test1)

print(result)