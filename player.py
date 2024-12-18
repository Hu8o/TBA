# Define the Player class.

from item import Inventory

class Player():
    """
    Représente un joueur dans un système de navigation textuelle.

    Cette classe permet de modéliser un joueur qui peut se déplacer entre 
    différentes pièces dans un environnement défini.

    Attributs:
        name (str): Le nom du joueur.
        current_room (Room): La pièce actuelle dans laquelle se trouve le joueur.

    Méthodes:
        __init__(name):
            Initialise une instance de la classe avec un nom et une pièce actuelle initiale (None).
        move(direction):
            Permet au joueur de se déplacer vers une autre pièce dans une direction donnée.

    Exceptions:
        Cette classe ne lève pas directement d'exception, mais la méthode `move` 
        suppose que les sorties dans `current_room` sont correctement définies.

    Exemples d'utilisation:
    >>> player = Player("Alex")
    >>> player.name
    'Alex'
    >>> player.current_room is None
    True
    >>> salon = Room("Salon", "un salon spacieux et lumineux.")
    >>> cuisine = Room("Cuisine", "une cuisine bien équipée.")
    >>> salon.exits['nord'] = cuisine
    >>> player.current_room = salon
    >>> player.move("nord")
    ...
    Vous êtes une cuisine bien équipée.
    
    Sorties: 
    True
    >>> player.current_room == cuisine
    True
    >>> player.move("sud")
    ...
    Aucune porte dans cette direction !
    False
    """

    # Define the constructor.
    def __init__(self, name,max_weight=10):
        self.name = name
        self.current_room = None
        self.previous_room=None
        self.history=[]
        self.inventory=Inventory()
        self.max_weight = max_weight  # Poids maximum transportable

    def current_inventory_weight(self):
        """
        Calcule le poids total des objets dans l'inventaire du joueur.

        Returns:
            float: Le poids total des objets.
        """
        return sum(item.weight for item in self.inventory)

 
    # Define the move method.
    def move(self, direction):

        next_room = self.current_room.exits[direction]
        
        if self.current_room is None:
            print("\n Erreur:Le joueur n'est pas dans une pièce !\n")
            return False

        self.previous_room = self.current_room
       
        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Mettre à jour la pièce actuelle
        self.current_room = next_room


        if self.current_room not in self.history:
            self.history.append(self.current_room.name)
        print(self.current_room.get_long_description())
        return True
 

    def back(self):
        """
        Permet au joueur de revenir à la pièce précédente.

        Returns:
            bool: True si le retour en arrière a réussi, False sinon.
        """
        if self.previous_room is None:
            print("\nErreur : Vous ne pouvez pas revenir en arrière car vous n'avez pas encore effectué de déplacement.\n")
            return False

        # Inverser la pièce actuelle et la pièce précédente
        self.current_room, self.previous_room = self.previous_room, self.current_room

        print(self.current_room.get_long_description())
        return True

    def get_history(self):
        if not self.history:
            return "Vous n'avez visité aucune pièce pour l'instant."

        history_string = "\nVous avez déjà visité les pièces suivantes:\n"
        for room_name in self.history:
            history_string += f"    - {room_name}\n"
        return history_string

    def get_inventory(self):
        return self.inventory.get_inventory()

    def look(self):
        """
        Affiche les détails de la pièce actuelle, y compris les items présents.
        """
        if self.current_room is None:
            print("Vous n'êtes pas dans une pièce.")
            return
        print(self.current_room.get_long_description())