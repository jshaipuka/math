def bubble_sort(arr):
  for j in range(len(arr), 1, -1):
    for i in range(1, j):
      if arr[i] < arr[i - 1]:
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
  return arr


test = [7, 2, 3, 1, 5]

print(bubble_sort(test))