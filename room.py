# Define the Room class.
from item import Inventory

class Room:

    """
    Représente une pièce dans un système de navigation.

    Cette classe permet de définir une pièce avec un nom, une description, 
    et des sorties possibles menant vers d'autres pièces. Elle est utilisée 
    pour modéliser un environnement de navigation textuelle.

    Attributs:
        name (str): Le nom de la pièce.
        description (str): Une description textuelle de la pièce.
        exits (dict): Un dictionnaire associant des directions (str) à 
                      d'autres objets `Room`.

    Méthodes:
        __init__(name, description):
            Initialise une instance de la classe avec un nom et une description.
        get_exit(direction):
            Retourne la pièce associée à une direction donnée, ou None si aucune 
            pièce n'existe dans cette direction.
        get_exit_string():
            Retourne une chaîne listant les directions disponibles.
        get_long_description():
            Retourne une description détaillée de la pièce, incluant ses sorties.

    Exceptions:
        Cette classe ne lève pas directement d'exception, mais les méthodes 
        peuvent échouer si des arguments non conformes sont fournis.

    Exemples d'utilisation:
    >>> kitchen = Room("Cuisine", "une cuisine bien équipée.")
    >>> kitchen.name
    'Cuisine'
    >>> kitchen.description
    'une cuisine bien équipée.'
    >>> kitchen.exits
    {}
    >>> salon = Room("Salon", "un salon confortable.")
    >>> kitchen.exits['sud'] = salon
    >>> kitchen.get_exit("sud") == salon
    True
    >>> kitchen.get_exit_string()
    'Sorties: sud'
    >>> print(kitchen.get_long_description())
    ...
    Vous êtes une cuisine bien équipée.
    
    Sorties: sud
    """

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = Inventory() # Initialisation de l'inventaire à vide
        self.items = []  # Initialisation des items de la pièce


    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
       return f"\n Vous êtes {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        return self.inventory.get_inventory()