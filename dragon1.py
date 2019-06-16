def addToInventory(inventory, addItems):
    print("inventory:")
    for item in addItems:
        if item in inventory:
            inventory[item] += 1
            
        else:
            inventory[item] = 1  
    print(str(item), inv)       
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)