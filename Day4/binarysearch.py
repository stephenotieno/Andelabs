class BinarySearch(list):

	def __init__(self,a,b):
		self.b = b
		self.a = a
		our_list = []
		our_list.append(b)		
		len_of_list = 1
		while len_of_list < a:
			our_list.append(our_list[len_of_list - 1] + b)
			len_of_list = len_of_list + 1
		super(BinarySearch, self).__init__(our_list)
		self.length = len(our_list)

	def search(self,item):
		first = self.b
		last = self.length-1
		found = False

		while first <= last and not found:
			if self.a/2 == item:
				found = True
			elif item < self.a/2:
				last = midpoint-1
			else:
				first = midpoint+1

		return found

one_to_twenty = BinarySearch(20,1)
search = one_to_twenty.search(16)

print search

