class MissingNumbers(object):

	def __init__(self, array1, array2):
		self.array1 = array1
		self.array2 = array2


	def find_missing(self, array1, array2):
		if len(self.array1) == len(self.array2):
			return 0
		
		if len(self.array1) > len(self.array2):
			first_list = self.array1
			second_list = self.array2
		else:
			first_list = self.array2
			second_list = self.array1

			for item in first_list:
				if item in second_list:
					pass
				else:
					return item

def main():

	list_miss_num = []

	check = MissingNumbers("array1","array2")
	num_miss = check.find_missing(array1,array2)

	list_miss_num.append(check)

	print list_miss_num






