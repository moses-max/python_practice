def string2(list):
    s = ""
    for i in range(len(list)):
        if i > 0:
            if i == len(list) - 1:
                s = s + " and "
            else:
                s = s + ", "
        s = s + list[i]
    return s