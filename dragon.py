def addToInventory(inventory, addItems):
    print("inventory:")
    for item in addItems:
        if item in inventory:
            inventory[item] += 1
            
        else:
            inventory[item] = 1  
    return inventory       
def displayInventory(inv):
    total = 0
    for item in inv:
        total += inv[item]
        print(inv[item], item)
    print('Total number of items: ' + (str(total)))    # displays the total number of items in the dictionary
    
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = addToInventory(inv, dragonLoot)
displayInventory(inventory)