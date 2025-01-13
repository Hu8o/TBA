# Define the Player class.

class Player():
    """
    Représente un joueur dans un système de navigation textuelle.

    Cette classe permet de modéliser un joueur qui peut se déplacer entre 
    différentes pièces dans un environnement défini.

    Attributs:
        name (str): Le nom du joueur.
        current_room (Room): La pièce actuelle dans laquelle se trouve le joueur.
        previous_room (Room): La dernière pièce visitée.
        history (list): Liste des pièces déjà visitées.
        inventory (dict): Inventaire du joueur, avec les noms des items comme clés 
                          et les objets Item comme valeurs.
        max_weight (float): Poids maximum que le joueur peut transporter.

    Méthodes:
        __init__(name, max_weight=10):
            Initialise une instance de la classe avec un nom, un poids maximum 
            et un inventaire vide.
        move(direction):
            Permet au joueur de se déplacer vers une autre pièce dans une direction donnée.
        back():
            Permet au joueur de revenir à la pièce précédente.
        get_history():
            Retourne l'historique des pièces visitées.
        add_to_inventory(item):
            Ajoute un item à l'inventaire du joueur.
        remove_from_inventory(item_name):
            Retire un item de l'inventaire du joueur.
        current_inventory_weight():
            Calcule le poids total des objets dans l'inventaire.
        look():
            Affiche les détails de la pièce actuelle.
    """

    def __init__(self, name, max_weight=10):
        self.name = name
        self.current_room = None
        self.previous_room = None
        self.history = []
        self.inventory = {}  # Initialisation d'un inventaire vide
        self.max_weight = 5  # Poids maximum transportable

    def current_inventory_weight(self):
        """
        Calcule le poids total des objets dans l'inventaire du joueur.

        Returns:
            float: Le poids total des objets.
        """
        return sum(item.weight for item in self.inventory.values())

    def move(self, direction):
        if self.current_room is None:
            print("\nErreur: Le joueur n'est pas dans une pièce !\n")
            return False

        next_room = self.current_room.exits.get(direction, None)

        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        self.previous_room = self.current_room
        self.current_room = next_room

        if self.current_room.name not in self.history:
            self.history.append(self.current_room.name)

        print(self.current_room.get_long_description())
        return True

    def back(self):
        """
        Permet au joueur de revenir à la pièce précédente.

        Returns:
            bool: True si le joueur est revenu à la pièce précédente, False sinon.
        """
        if self.previous_room is None:
            print("\nIl n'y a aucune pièce précédente à laquelle revenir.\n")
            return False

        self.current_room, self.previous_room = self.previous_room, self.current_room
        print(f"\nVous êtes retourné dans la pièce précédente : {self.current_room.name}\n")
        return True
        
    def get_history(self):
        """
        Retourne une description des pièces visitées par le joueur.

        Returns:
            str: Liste des pièces visitées.
        """
        if not self.history:
            return "Vous n'avez visité aucune pièce pour l'instant."

        history_string = "\nVous avez déjà visité les pièces suivantes:\n"
        for room_name in self.history:
            history_string += f"    - {room_name}\n"
        return history_string

    def add_to_inventory(self, item):
        """
        Ajoute un item à l'inventaire du joueur.

        Args:
            item (Item): L'objet à ajouter.

        Returns:
            bool: True si l'ajout a réussi, False si le poids total est dépassé.
        """
        if self.current_inventory_weight() + item.weight > self.max_weight:
            print(f"\nVous ne pouvez pas ajouter {item.name} à votre inventaire, car il dépasse le poids maximum autorisé ({self.max_weight} kg).\n")
            return False

        self.inventory[item.name] = item
        print(f"\n{item.name} a été ajouté à votre inventaire.\n")
        return True

    def remove_from_inventory(self, item_name):
        """
        Retire un item de l'inventaire du joueur.

        Args:
            item_name (str): Le nom de l'objet à retirer.

        Returns:
            bool: True si l'objet a été retiré, False s'il n'est pas dans l'inventaire.
        """
        if item_name not in self.inventory:
            print(f"\n{item_name} n'est pas dans votre inventaire.\n")
            return False

        del self.inventory[item_name]
        print(f"\n{item_name} a été retiré de votre inventaire.\n")
        return True

    def get_inventory(self):
        """
        Retourne une liste des objets dans l'inventaire.

        Returns:
            str: Description des objets dans l'inventaire.
        """
        if not self.inventory:
            return "Votre inventaire est vide."

        inventory_string = "\nVotre inventaire contient les objets suivants:\n"
        for item_name, item in self.inventory.items():
            inventory_string += f"    - {item_name}: {item.description} (Poids: {item.weight} kg)\n"
        return inventory_string

   
