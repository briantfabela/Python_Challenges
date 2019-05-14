# Small code challenges involving Python dictionaries

# Dictionary Provided
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Create a function to display a dictionary as an inventory of a fantasy game
def displayDictionary(inventory):
    print('Inventory:')
    item_total=0 # item total to be display at end of function
    for key, val in inventory.items(): # iterate thorugh dictionary
        print(val, key) # display the amount and the respective item
        item_total+=val # add this to item_total variable 
    print("Item Total: ", item_total) # print the item_total variable

# provided variables to test code with
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Function to generate list of unique items from a loot list with duplicates
def itemList(loot): # takes a list of loot items and returns the list without duplicates
    inventoryItems = [] # list that will contain unique items

    for item in loot: # iterate through all loot items
        if item not in inventoryItems: # if the item is not already in list
            inventoryItems.append(item) # add the item at the end
    
    return inventoryItems

# generate dictionary with items in loot and their amount (in inventory format)
def countLoot(loot): # counts each instance of an item and returns an inventory dictionary
    keys = itemList(loot) # generate the list of unique items
    lootInventory = dict() # create empty dictionary for the inventory

    for key in keys: # iterate through items and count the amount of times that item occurs
        lootInventory[key] = loot.count(key) # item = the amount of the item in loot list
    
    return lootInventory # return the inventory dictionary

# add a list of loot items to a current inventory
def addToInventory(inventory, addItems):
    
    loot = countLoot(addItems) # get a inventory dictionary of the loot items

    for key, val in loot.items(): # for each item in loot
        if key not in inventory: # if item not in inventory
            inventory[key] = loot[key] # add item and count to inventory
        else:
            inventory[key] += loot[key] # add items to those already in inventory

def main():
    addToInventory(inv, dragonLoot)
    displayDictionary(inv)

if __name__ == "__main__":
    main()