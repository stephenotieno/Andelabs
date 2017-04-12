def find_max_min(Array):
    length = len(Array)
    max = Array[0]
    min = Array[0]
    
    for item in Array:
        if item < min:
            min = item
        else:
            pass
    
    for item in Array:
        if item > max:
            max = item
        else:
            pass
                
    if max == min:
        return length
    else:
        return [min, max]
