def find_max_min(array):
	min = array[0]
	for item in array:
		if item < min:
			min = item
		else:
			pass

	max = array[1]
	for item in array:
		if item > max:
			max = item
		else:
			pass

	return [min, max]


