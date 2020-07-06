def partition(arr, left, right):
  pivot = arr[right]
  smallerIndex = left - 1

  for i in range(left, right):
    is_pivot_larger_than_current_value = arr[i] <= pivot
  
    if is_pivot_larger_than_current_value:
      smallerIndex += 1
      arr[smallerIndex], arr[i] = arr[i], arr[smallerIndex]
  

  smallerIndex += 1
  arr[smallerIndex], arr[right] = arr[right], arr[smallerIndex]

  return smallerIndex


# choose pivot
# smaller < pivot < greater
# sort left such as smaller < pivot
# sort right such as pivot < greater
def quick_sort(arr, left, right):
  if right - left > 0: # in bounds
    pivot = partition(arr, left, right)

    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1,  right)



test = [7, 2, 3, 1, 5]

quick_sort(test, 0, len(test) - 1)
print(test)