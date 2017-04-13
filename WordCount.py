def words(String):
    word_count = dict()
    words = String.split()
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
        
