SHELL = lambda i: i // 2

def insertion_sort(array, stepf):
	n = len(array)
	increment = stepf(n) ## increment by step

	# while increment is 1+
	while increment > 0:

		# from 0 to increment do insertionSort with step|gap
		for startPosition in range(increment):
			stepInsertionSort(array, startPosition, increment)

		print("Incrementing by", increment,". Sorted array:", array)

		increment = stepf(increment)
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
		
test = [5,2,3,1,7]

print(insertion_sort(test, SHELL))
		