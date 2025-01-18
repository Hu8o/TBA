"""
Module item.py

Ce module contient les classes représentant des objets que le joueur peut trouver et manipuler
dans le jeu, ainsi qu'une classe Inventory pour gérer un inventaire d'objets.
"""

class Item:
    """
    Représente un objet que le joueur peut trouver dans différents lieux de la carte.

    Attributs :
        name (str) : Le nom de l'objet.
        description (str) : Une description de l'objet.
        weight (float) : Le poids de l'objet en kilogrammes (peut être un int ou un float).

    Méthodes :
        __init__(name, description, weight) : Initialise les attributs de l'objet.
        __str__() : Retourne une représentation textuelle de l'objet.
    """

    def __init__(self, name: str, description: str, weight: float):
        """
        Initialise un nouvel objet avec un nom, une description et un poids.

        Args :
            name (str) : Le nom de l'objet.
            description (str) : Une description de l'objet.
            weight (float) : Le poids de l'objet en kilogrammes.
        """
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self) -> str:
        """
        Retourne une représentation textuelle de l'objet.

        Returns :
            str : Une chaîne décrivant l'objet.
        """
        return f"{self.name} : {self.description} ({self.weight} kg)"


class Inventory:
    """
    Représente un inventaire pouvant contenir des objets.

    Attributs :
        items (list[Item]) : Liste des objets présents dans l'inventaire.

    Méthodes :
        add_item(item: Item) : Ajoute un objet à l'inventaire.
        remove_item(item: Item) : Retire un objet de l'inventaire si il est présent.
        is_empty() -> bool : Vérifie si l'inventaire est vide.
        get_inventory() -> str : Retourne une chaîne décrivant le contenu de l'inventaire.
    """

    def __init__(self):
        """ Initialise un inventaire vide. """
        self.items = []

    def add_item(self, item: Item):
        """
        Ajoute un objet à l'inventaire.

        Args :
            item (Item) : L'objet à ajouter à l'inventaire.
        """
        self.items.append(item)

    def remove_item(self, item: Item):
        """
        Retire un objet de l'inventaire si il est présent.

        Args :
            item (Item) : L'objet à retirer de l'inventaire.
        """
        if item in self.items:
            self.items.remove(item)

    def is_empty(self) -> bool:
        """
        Vérifie si l'inventaire est vide.

        Returns :
            bool : True si l'inventaire est vide, False sinon.
        """
        return len(self.items) == 0

    def get_inventory(self) -> str:
        """
        Retourne une chaîne décrivant le contenu de l'inventaire.

        Returns :
            str : La description des objets dans l'inventaire.
        """
        if self.is_empty():
            return "Il n'y a rien ici."

        inventory_string = "L'inventaire contient :\n"
        inventory_string += "\n".join([f"    - {item}" for item in self.items])
        return inventory_string
