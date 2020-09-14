#################################### helpers

import random, math

def generate_random_sequence(start, finish, max_items):
  arr = []

  for i in range(0, max_items):
    arr.append(round(random.uniform(start, finish), 2))

  return arr

#################################### sorting

def merge(arr):
  merged = [] # reuse array

  for i in range(0, len(arr)):
    merged.extend(arr[i])

  return merged

def insertion_sort(arr):
  # if len(arr) == 1 it is sorted
  for i in range(1, len(arr)):
    # go over previous values with decremeting each time
    while i > 0 and arr[i] < arr[i - 1]:
      # if current is smaller than previous, swap
      arr[i], arr[i - 1] = arr[i - 1], arr[i]
      i = i - 1
  return arr

def bucket_sort(arr, a, b):
  n = len(arr)
  buckets = [ [] for _ in range(n) ] # problema. Esli bakety dovoljno boljshie, to u nas problemy (naprimer vse v 1 bucket). Esli slishkom malenjkij bucket (namprer v 1 bcukete 1 element, a v drugom buckete 10 elementov. POluchaetsja neravnomerno). 4toby najti razmer bucketa nuzna predvariteljnaja operacija. Mozhno pereborom.
# mozhet 4to-to svjazannoe s logn?

  for i in range(n):
    value = arr[i]
    bucket_index = math.floor(n * value)
    buckets[bucket_index].append(value)

  for bucket_index in range(len(buckets)):
    buckets[bucket_index] = insertion_sort(buckets[bucket_index])

  print('buckets', buckets)

  return merge(buckets)

#################################### main

a = 0
b = 1

test = generate_random_sequence(a, b, 10)

print('sorted sequence', bucket_sort(test, a, b))
print('initial sequence', test)