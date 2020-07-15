# Написать сортировку подсчетом для последовательности, где все элементы имеют значение от a до b

#################################### helpers

import random

def generate_random_sequence_from_alphabet(max_items, alphabet):
  n = len(alphabet)
  arr = []

  for _ in range(0, max_items):
    arr.append(alphabet[random.randrange(n)])

  return arr

#################################### sorting

# alphabet is distinct and sorted
def counting_sort(arr, alphabet):
  counter = dict.fromkeys(alphabet, 0)

  for i in range(0, len(arr)):
    letter = arr[i]
    counter[letter] += 1
  
  arr = [] # reuse array

  for letter, count in counter.items():
    print('There are ', count, letter)
    arr.extend([letter]*count)
  
  return arr


#################################### main

alphabet = ['a', 'b']
test = generate_random_sequence_from_alphabet(10, alphabet)

print('initial sequence', test)
print('sorted sequence', counting_sort(test, alphabet))