class BinarySearch(list):
    def __init__(self,  a,  b):
        self.a = a
        self.b = b
        Array = range(b,  a+b,  b)
        self.Array = Array
        length = len(Array)
        self.length = length
        
    def search(self,  num):
        first = 0
        last = self.length - 1
        found = False
        list(enumerate(self.Array))
        count = 0
        
        while first <= last and not found:
            count += 1
            midpoint = (first + last)//2
            if self.Array[midpoint] == num:
                found = True
            else:
                if num < self.Array[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
                    
                    for i, j in enumerate(self.Array):
                        if j == num:
                            index = i
                                            
                            return_value = dict([('count',  count),  ('index',  index)])
                            return return_value
            
