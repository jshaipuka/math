def transform_into_heap(arr, n, root):
  largest = root
  left = 2 * root + 1
  right = 2 * root + 2

  is_left_child_larger_than_root = left < n and arr[root] < arr[left]
  is_right_child_larger_than_root = right < n and arr[root] < arr[right]

  if is_left_child_larger_than_root:
    largest = left # new largest
  
  if is_right_child_larger_than_root:
    largest = right # new largest

  has_root_changed = largest != root
  if has_root_changed:
    arr[root], arr[largest] = arr[largest], arr[root]
    transform_into_heap(arr, n, largest)


def heap_sort(arr):
  n = len(arr)

  # build heap
  for i in range(n // 2 - 1, 0, -1):
    transform_into_heap(arr, n, i)

  # extract element one by one
  for last_node in range(n - 1, 0 , -1):
    arr[last_node], arr[0] = arr[0], arr[last_node] # swap first and last heap node
    transform_into_heap(arr, last_node, 0)
  
  return arr

test = [7, 2, 3, 1, 5]

print(heap_sort(test))
# Ne rabotaet
# Result: [1, 5, 2, 3, 7]
