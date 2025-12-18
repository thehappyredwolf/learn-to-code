def merge(dict1, dict2):
    result = {}
    for key in dict1:
        result[key] = dict1[key]
    for key in dict2:
        result[key] = dict2[key]
    return result
