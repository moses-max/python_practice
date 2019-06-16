players_Stuff = {"arrow": 12, "gold coin": 42, "rope": 1, "torch": 6, "dagger": 1, }

def displayInventory(inventory):
    print("Inventory:")
    player_item = 0
    for ke, it in inventory.items():
        print(str(it) + ' ' + ke)
        player_item += it
    print("Total number of items: " + str(player_item))

displayInventory(players_Stuff)