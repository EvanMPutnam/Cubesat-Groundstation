DOUBLE_ARR = "Double_Arr"
INTEGER_ARR = "Integer_Arr"
DOUBLE = "Double"
INT = "Int"

def verify_data(data, data_type):
    data = data.replace("[", "")
    data = data.replace("]", "")
    #Verify singular double
    if data_type == DOUBLE:
        return is_Double(data), str(data)
    #Verify singular int
    elif data_type == INT:
        return is_Integer(data), str(data)
    #Verify double array
    elif data_type == DOUBLE_ARR:
        lst = data.split(',')
        newly_formatted_lst = []
        for i in lst:
            if not is_Double(i.strip()):
                return False, []
            newly_formatted_lst.append(float(i.strip()))
        return True, newly_formatted_lst
    #Verify integer array
    elif data_type == INTEGER_ARR:
        lst = data.split(',')
        newly_formatted_lst = []
        for i in lst:
            if not is_Integer(i.strip()):
                return False, []
            newly_formatted_lst.append(int(i.strip()))
        return True, newly_formatted_lst
    return False, []

def is_Integer(number_to_check):
    try:
        int(number_to_check)
        return True
    except ValueError:
        return False

def is_Double(number_to_check):
    try:
        float(number_to_check)
        return True
    except ValueError:
        return False