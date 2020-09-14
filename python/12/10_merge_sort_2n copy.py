# Написать сортировку слиянием с массивом длины 2n
# 2n это массив чётной длины?

# РЕШЕНИЕ СПИСАНО И НЕПОНЯТО. И не совсем работает.
def merge(AB, n, C):
    C[:] = AB[n:]

    a, b, r = n - 1, len(C) - 1, len(AB) - 1
    while True:
        if AB[a] > C[b]:
            AB[r] = AB[a]
            a -= 1
            if a < 0:
                AB[a:r] = C[:b]
                return
        else:
            AB[r] = C[b]
            b -= 1
            if b < 0:
                return
        r -= 1
  

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