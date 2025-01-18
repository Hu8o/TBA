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
        self.characters=[]

    def add_character(self, character):
        """
        Ajoute un personnage à la pièce.
        """
        self.characters.append(character)
        character.current_room = self
    
    def add_item(self, item):
        """
        Ajoute un item à la pièce.
        """
        self.items.append(item)
        item.current_room = self

    def get_characters_description(self):
        """
        Retourne une description des personnages présents dans la pièce.
        """
        if not self.characters:
            return "Il n'y a personne ici."
        descriptions = [f"- {char.name}: {char.description}" for char in self.characters]
        return "Vous voyez ici :\n" + "\n".join(descriptions)

    
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

    def get_item_by_name(self, item_name):
        """
        Recherche un item par son nom dans la pièce.

        Args:
            item_name (str): Le nom de l'item recherché.

        Returns:
            Item: L'item correspondant, ou None si non trouvé.
        """
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def get_character_by_name(self, character_name):
        """
        Recherche un personnage par son nom dans la pièce.

        Args:
            character_name (str): Le nom du personnage.

        Returns:
            Character: Le personnage correspondant, ou None si non trouvé.
        """
        for character in self.characters:
            if character.name.lower() == character_name.lower():
                return character
        return None
