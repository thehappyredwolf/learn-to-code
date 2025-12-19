def join_strings(strings):
    joined_string = ""
    for i in range(len(strings)):
        if (i == len(strings) - 1):
            joined_string += strings[i]
        else:
            joined_string += strings[i] + ","
    return joined_string
