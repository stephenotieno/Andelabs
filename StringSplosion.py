def StringSplosion(string):
    string_characters = list(string)
    string_plosion = []
    n = len(string_characters)
    i = 1

    for item in string_characters:
        string_plosion.append(item)
       
    while i < n:
        string_characters = string_characters[0:-1]
        for item in reversed(string_characters):
            string_plosion.insert(0, item)
        i +=1
        
    result = ''.join(string_plosion)
    
    return (result)
