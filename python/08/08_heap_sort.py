def find_largest_node_index(arr, n, root):
  largest_node = root
  left = 2 * root + 1
  right = 2 * root + 2
  
  # set left as largest if applicable
  if left < n and arr[root] < arr[left]:
    largest_node = left

  # set right as largest if right is bigger than current largest (left or root)
  if right < n and arr[largest_node] < arr[right]:
    largest_node = right

  return largest_node

def transform_into_heap(arr, n, root):
  largest = find_largest_node_index(arr, n, root)

  if largest != root:
    arr[root], arr[largest] = arr[largest], arr[root]
    transform_into_heap(arr, n, largest)


def heap_sort(arr):
  first = 0
  n = len(arr)
  first_not_leaf = n // 2 - 1

  # build heap
  for i in range(first_not_leaf, -1, -1):
    transform_into_heap(arr, n, i)

  for last in range(n - 1, 0 , -1):
     # swap first and last heap node
    arr[last], arr[first] = arr[first], arr[last]
    transform_into_heap(arr, last, first)
  
  return arr

test = [7, 2, 3, 1, 5]

print(heap_sort(test))