def find_missing(list1, list2):
    if len(list1) == 0 or len(list2) == 0:
        return 0
    elif list1 == list2:
        return 0
    else:
        if len(list1) > len(list2):
            first_list = list1
            second_list = list2
        else:
            first_list = list2
            second_list = list1
        for item in first_list:
            if item not in second_list:
                return item

    
