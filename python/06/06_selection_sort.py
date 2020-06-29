# always select min
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


test = [7,2,3,1,5]

print(selection_sort(test))