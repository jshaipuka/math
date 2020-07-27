# Написать сортировку слиянием с массивом длины 2n
# 2n это массив чётной длины?

# РЕШЕНИЕ СПИСАНО И НЕПОНЯТО. И не совсем работает.

def merge(array, leftPointer, half, rightPointer):
  leftIndex = half
  rightIndex = half + 1

  # Two pointers to maintain start 
  # of both arrays to merge 
  while (leftPointer <= leftIndex and rightIndex <= rightPointer): 

      # If element 1 is in right place 
      if (array[leftPointer] <= array[leftIndex]): 
          leftPointer += 1
      else: 
          value = array[leftIndex]
          index = leftIndex

          # Shift all the elements between element 1 
          # element 2, right by 1. 
          while (index != leftPointer): 
              array[index] = array[index - 1]
              index -= 1
            
          array[leftPointer] = value

          # Update all the pointers 
          leftPointer += 1
          half += 1
          leftIndex += 1
  return array
  

def sort2(array, left, right):
  if left - right == 0: # all sorted
    return array
  else:
    half = (left + right) // 2
    sort2(array, left, half) # left half sorted
    sort2(array, half + 1, right) # right half sorted
    return merge(array, left, half, right)


def sort(array):
  return sort2(array, 0, len(array) - 1)

test = [1,4,5,2,4,1,9]
result = sort(test)

print(result) # [1, 2, 1, 4, 4, 5, 9]