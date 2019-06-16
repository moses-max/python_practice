Stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayinventory(inventory):
    print("inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v)+ ''+(k))
        item_total += v
    print('Total numbers of items: ' +str(item_total))

displayinventory(stuff)