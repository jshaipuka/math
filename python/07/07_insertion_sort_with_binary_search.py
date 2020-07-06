def binary_search(arr, search_value, start, finish):
  while start < finish:
    mid = (finish + start) // 2

    if search_value < arr[mid]:
      finish = mid - 1
    elif search_value > arr[mid]: 
      start = mid + 1
    else:
      return mid
  return -1 


# binary search doen't work because array must be sorted.

def insertion_sort_with_binary_search(arr):
  # if len(arr) == 1 it is sorted
  for i in range(1, len(arr)):
    previous = i - 1
    search_value = arr[i]

    found = binary_search(arr, search_value, 0, i)

    while previous >= found:
      arr[previous + 1] = arr[previous]
      previous = previous - 1
    
    arr[previous + 1] = search_value

  return arr


test = [7, 2, 3, 1, 5]

print(insertion_sort_with_binary_search(test))

# Ne rabotaet