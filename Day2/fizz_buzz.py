def fizz_buzz (input_number):
	if input_number%15 == 0:
		output = "FizzBuzz"
	elif input_number%5 == 0:
		output = "Buzz"
	elif input_number%3 == 0:
		output = "Fizz"
	else:
		output = input_number

	return output
