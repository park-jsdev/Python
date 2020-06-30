#!/usr/bin/env python

# Fantasy Game Dragon Loot

def display_inventory(inventory):
    total = 0
    print ('Inventory:')
    for k, v in inventory.items():
        print (str(v)+' ' + k)
        total += v
    print ('Total number of items: '+ str(total))

# Add Loot to Inventory
def add_to_inventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(str(item), 0)
        inventory[item] += 1
    return inventory

if __name__ == '__main__':
    inventory = {'short sword': 1, 'torch': 1, 'gold coin': 10, 'dagger': 1}
    dragonLoot = ['Rune 2-handed Sword', 'The Ashbringer', 'Infinity Edge']
    inventory = add_to_inventory(inventory, dragonLoot)
    display_inventory(inventory)