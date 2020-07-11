def insert(array, currentIndex):
  key = array[currentIndex]
  index = currentIndex - 1
  while index >= 0 and array[index] > key:
    array[index + 1] = array[index]
    index = index - 1
  array[index + 1] = key
  
def insertion_sort(array, currentIndex):
  print('array', array, 'index', currentIndex)
  
  if currentIndex == 0:
    return currentIndex
  else:
     currentIndex = insertion_sort(array, currentIndex - 1)
     insert(array, currentIndex)
     return currentIndex + 1

insertion_sort(array, len(array))

print(array)