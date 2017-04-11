def arith_geo(Array):
    n = len(Array)
    if n == 0:
        value = 0
    elif n != 0:
        constant = Array[1] - Array[0]
        for i in range(n-1):
            if Array[i+1] - Array[i] == constant:
                value = 'Arithmetic'
            elif (Array[i+1] - Array[i] != constant):
                constant = Array[2]/Array[1]
                for i in range(n-1):
                    if Array[i+1]/Array[i] != constant:
                        value = -1
                    else:
                        value = 'Geometric'
    return value
