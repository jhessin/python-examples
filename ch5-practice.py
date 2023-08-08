inventory = {
        'rope': 1,
        'torch': 6,
        'gold coin': 42,
        'dagger': 1,
        'arrow': 12,
        }

def displayInventory(inv: dict[str, int]):
    print('Inventory:')
    sum = 0
    for k, v in inv.items():
        print(v, k)
        sum += v
    print()
    print('Total number of items:', sum)

def addToInventory(inv: dict[str, int], addedItems: list[str]):
    for item in addedItems:
        inv.setdefault(item, 0)
        inv[item] += 1

displayInventory(inventory)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inventory, dragonLoot)
displayInventory(inventory)
