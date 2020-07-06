import math

phi = (1 + math.sqrt(5)) / 2
gap_factor = 1/(1 - math.exp(-phi)) # = 1.2473309501

def comb_sort(arr):
  n = len(arr)

  gap = math.floor(n // gap_factor) # gap or step

  while gap > 0:
    i = 0 # first index in arr
    for j in range(gap, n): # first index after gap
      if arr[j] < arr[i]: 
        arr[i], arr[j] = arr[j], arr[i]
      i += 1 # at the end of loop, increment both indexes by one
    gap = math.floor(gap // gap_factor)
  return arr


test = [7, 2, 3, 1, 5]

print(comb_sort(test))
