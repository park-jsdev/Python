#!/usr/bin/env python

# Fantasy Game Inventory

def display_inventory(inventory):
    total = 0
    print ('Inventory:')
    for k, v in inventory.items():
        print (str(v)+' ' + k)
        total += v
    print ('Total number of items: '+ str(total))



if __name__ == '__main__':
    inventory = {'short sword': 1, 'torch': 1, 'gold coin': 10, 'dagger': 1}
    display_inventory(inventory)