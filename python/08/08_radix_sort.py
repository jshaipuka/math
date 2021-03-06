#################################### helpers

import random

def generate_random_sequence_from_alphabet(max_items, max_digits, alphabet):
  n = len(alphabet)
  arr = []

  for i in range(0, max_items):
    value = [0]*max_digits
    for j in range(0, max_digits):
      value[j] = alphabet[random.randrange(n)]
    arr.append(''.join(str(v) for v in value))

  return arr

#################################### sorting

# alphabet is distinct and sorted. Word length are the same
def radix_sort(arr, word_length, alphabet):
  groups = dict.fromkeys(map(str, alphabet), [])

  for check_digit in range(word_length, 0, -1):
    # groups = groups_initial.copy()

    for word_index in range(len(arr)):
      word = arr[word_index]
      digit = word[check_digit - 1]

      if digit in groups:
        groups[digit].append(word)
  
    arr = [] # reuse array

  for group in groups.values():
    arr.extend(group)
  
  return arr


#################################### main

alphabet = [0, 1]
word_length = 3
test = generate_random_sequence_from_alphabet(10, word_length, alphabet)

print('sorted sequence', radix_sort(test, word_length, alphabet))
print('initial sequence', test)
