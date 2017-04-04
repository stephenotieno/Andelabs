def prime_numbers (n):
    for number in range (n):
        for element in range (2,number):
            if (number%element==0):
                break
            else:
                prime_numbers_in_range = []
                prime_numbers_in_range.append(number)
                return (prime_numbers_in_range)

    
