def listToString(list):
    if list[-1]:
        list.append('and '+str(list[-1]))
        list.remove(list[-2])
    for i in range(len(list)):
        print(''+list[i]+', ')

list = ['cat','dog','rat','elephant']
listToString(list)