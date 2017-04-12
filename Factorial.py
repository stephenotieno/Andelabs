def factorial(number):
    result = 1
    fact_num = range(1, number+1)
    for items in fact_num:
        result *= items
    return result
