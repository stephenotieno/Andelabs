def data_type(data):
    if type(data) == str:
        return len(data)
    elif type(data) == bool:
        return data
    elif type(data) == list:
        if len(data) < 3:
            return None
        else:
            return data[2]
    elif data == None:
        return 'no value'
    elif type(data) == int:
        if data < 100:
            return'less than 100'
        elif data > 100:
            return'greater than 100'
