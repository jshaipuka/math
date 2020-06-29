import math

HIBBARD = lambda i: 2**i - 1

def insertion_sort(array, stepf):
	n = len(array)

	# if 2^x - 1 < n then x < log2(n - 1)
	# will not work for 2^0 - 1 = 0; 2^1 - 1 = 1
	# should be log2(n - 1) > 0
	limit = math.log(n - 1, 2)

	# if log2(n - 1) > 0 then n-1 > 1 => n > 2
	increment = 1 if n <= 2 else stepf(math.floor(limit))

	while increment > 0:

  	for startPosition in range(increment):
  		stepInsertionSort(array, startPosition, increment)
  
  	print("Incrementing by", increment,". Sorted array:", array)
  
  	increment = stepf(increment) if stepf(increment) < increment else increment // 2
	return array


def stepInsertionSort(array, start, step):
  # from starting postion + "step" until array end do sorting with incrementing by "step"
	for position in range(start + step, len(array), step):
		currentvalue = array[position]

		# while current position is bigger than step and current value is less than value from current position - step
		while position >= step and array[position - step] > currentvalue:
			# swap and decrement position
			array[position], array[position - step] = array[position - step], array[position]
			position = position - step
		
test = [5, 1, 4, 5, 6, 7, 8, 2, 1, 11 , 123, 2345, 4]

print(insertion_sort(test, HIBBARD))
		