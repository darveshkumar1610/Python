# Pet Shop Application
# Acts like a mini Inventory system

"""
Imports
Class
--init
--add
--remove
--display
--save
--load
Main
Test
"""

import json
import os.path

class Inventory:
    pets = {}                           # Class Variables

    def __init__(self):                 # Constructor - Default Actions
        self.load()

    def add(self,key,qty):
        q = 0
        if key in self.pets:
            v = self.pets[key]
            q = v + qty
        else:
            q = qty
        self.pets[key] = q
        print(f'Added {qty} {key}: total = {self.pets[key]}')

    def remove(self,key,qty):
        q = 0
        if key in self.pets:
            v = self.pets[key]
            q = v - qty
        if q < 0:
            q = 0
        self.pets[key] = q
        print(f'Removed {qty} {key}: total = {self.pets[key]}')

    def display(self):
        for key, value in self.pets.items():
            print(f'{key} = {value}')

    def save(self):
        print('Saving inventory')
        with open('inventory.txt', 'w') as f:
            json.dump(self.pets,f)
        print('Saved!!')

    def load(self):
        print('Lading inventory')
        if not os.path.exists('inventory.txt'):
            print('Skipping, nothing to load')
            return
        with open('inventory.txt', 'r') as f:
            self.pets = json.load(f)
        print('Loaded!!')

def main():
    inv = Inventory()

    while True:
        action = input('Actions: add, remove, list, save, exit:')
        if action == 'exit':
            break
        if action == 'add' or action == 'remove':
            key = input('Enter an Animal: ')
            qty = int(input('Enter the Qty: '))             # Qty must be int.
            if action == 'add':
                inv.add(key, qty)
            if action == 'remove':
                inv.remove(key, qty)
        if action == 'list':
            inv.display()
        if action == 'save':
            inv.save()

    inv.save()

if __name__ == "__main__":
    main()