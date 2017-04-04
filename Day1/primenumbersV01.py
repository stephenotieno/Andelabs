def prime_numbers (n):
    for number in range (n):
        for element in range (1,number):
            if (number%element==0):
                break
            else:
                return (element)
    
