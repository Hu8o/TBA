# Define the Player class.
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
    def __init__(self, name):
        self.name = name
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    