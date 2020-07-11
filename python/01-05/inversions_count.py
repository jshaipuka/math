# ============= count inversions O(n^2)
array5 = [4, 5, 1, 2, 3]


def countInversions(array):
  count = 0
 
  for i in range(0, len(array)):
    for j in range(i + 1, len(array)):
      if array[i] > array[j]:
        count = count + 1
  return count

print('input', array5, 'inversions via O(n^2) = ', countInversions(array5))

# ============= count inversions O(nlogn) via merge sort
array4 = [4, 5, 1, 2, 3]


def mergeCountInversionsV2(left, right):
  leftArray = left[1]
  rightArray = right[1]
  count = left[0] + right[0]

  leftIndex, rightIndex = 0, 0
  leftArrayLength = len(leftArray)
  rightArrayLength = len(rightArray)
  
  sorted = []
  goingLeft = True


  while leftIndex < leftArrayLength or rightIndex < rightArrayLength:
    if rightIndex == rightArrayLength or (leftIndex < leftArrayLength and leftArray[leftIndex] <= rightArray[rightIndex]):
      sorted.append(leftArray[leftIndex])
      leftIndex = leftIndex + 1
      count = count + rightIndex
    else:
      sorted.append(rightArray[rightIndex])
      rightIndex = rightIndex + 1
    
  return [count, sorted]

    
def countInversionsV2(count, array):
  if len(array) == 1:
    return [count, array]
  else:
    half = int(len(array) / 2)
    firstHalf = array[:half]
    secondHalf = array[half:]
    
    return mergeCountInversionsV2(countInversionsV2(count, firstHalf), countInversionsV2(count, secondHalf))

print('input', array4, 'inversions via O(nlogn) = ', countInversionsV2(0, array4)[0])
