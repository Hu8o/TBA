# inventory.py

class Inventory:
    """
    Représente un inventaire pouvant contenir des objets.
    """
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def is_empty(self):
        return len(self.items) == 0

    def get_inventory(self):
        if self.is_empty():
            return "Il n'y a rien ici."
        
        inventory_string = "L'inventaire contient :\n"
        inventory_string += "\n".join([f"    - {item}" for item in self.items])
        return inventory_string
