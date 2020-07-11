# Написать сортировку подсчетом для последовательности, где все элементы имеют значение от a до b

#################################### helpers

import random

def generate_random_sequence_from_alphabet(max_items, alphabet):
  n = len(alphabet)
  arr = []

  for i in range(0, max_items):
    arr.append(alphabet[random.randrange(n)])

  return arr

#################################### sorting

# alphabet is distinct and sorted
def counting_sort(arr, alphabet):
  count = [0]*len(alphabet)

  for i in range(0, len(arr)):
    letter = arr[i]
    letter_sort_index = alphabet.index(letter)
    count[letter_sort_index] += 1
  
  arr = [] # reuse array

  for i in range(0, len(count)):
    print('There are ', count[i], alphabet[i])
    arr.extend([alphabet[i]]*count[i])
  
  return arr


#################################### main

alphabet = ['a', 'b']
test = generate_random_sequence_from_alphabet(10, alphabet)

print('initial sequence', test)
print('sorted sequence', counting_sort(test, alphabet))