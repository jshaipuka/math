# Notes
# Merge sort использовать на верхний уровнях
# insertion|selection на нижних уровнях

# Ocenka:
# N*logN if N / 2 < 10 else 2 * (N / 2) ^2

def selection_sort(arr):
  for currentIndex in range(0, len(arr)):
    if currentIndex == len(arr) - 1:
      break
    else:

      # select min
      minIndex = currentIndex
      for newMinIndex in range(currentIndex + 1, len(arr)):
        if arr[newMinIndex] < arr[minIndex]:
          minIndex = newMinIndex

      # swap
      arr[currentIndex], arr[minIndex] = arr[minIndex], arr[currentIndex]

  return arr


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

def sort(array):
  big_array_limit = 2

  if len(array) == 1:
    return array
  else:
    half = len(array) // 2
    if half > big_array_limit:
      return merge(selection_sort(array[:half]), selection_sort(array[half:]))
    else:
      return merge(sort(array[:half]), sort(array[half:]))

test = [1,4,5,2,4,1,9]
result = sort(test)

print(result)