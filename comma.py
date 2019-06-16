myList = ['staples','ball','pencil','notepad']

def mystring(lst):
    lst = mylist
    if len(myList) > 0:
        lst.insert(-1, ' and ')
        return lst
    else:
        return mystring(lst)

mystring(lst)
