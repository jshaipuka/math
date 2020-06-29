def insertion_sort(arr):
	# if len(arr) == 1 it is sorted
	for i in range(1, len(arr)):
		# go over previous values with decremeting each time
		while i > 0 and arr[i] < arr[i - 1]:
			# if current is smaller than previous, swap
			arr[i], arr[i - 1] = arr[i - 1], arr[i]
			i = i - 1
	return arr


test = [7,2,3,1,5]

print(insertion_sort(test))
