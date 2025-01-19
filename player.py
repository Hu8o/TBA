# Définition de la classe Player.

class Player:
    """
    Représente un joueur dans un système de navigation textuelle.

    Cette classe modélise un joueur capable de se déplacer entre différentes pièces
    dans un environnement défini et d'interagir avec les objets.

    Attributs :
        name (str) : Nom du joueur.
        current_room (Room) : Pièce actuelle dans laquelle se trouve le joueur.
        previous_room (Room) : Dernière pièce visitée.
        history (list) : Liste des noms des pièces visitées.
        inventory (dict) : Inventaire du joueur (nom des items comme clés et objets Item comme valeurs).
        max_weight (float) : Poids maximum que le joueur peut transporter.

    Méthodes :
        __init__ : Initialise une instance de Player avec un nom et un poids maximum.
        current_inventory_weight : Calcule le poids total des objets transportés.
        move : Permet au joueur de se déplacer vers une pièce adjacente.
        back : Permet au joueur de revenir à la pièce précédente.
        get_history : Retourne l'historique des pièces visitées.
        add_to_inventory : Ajoute un item à l'inventaire du joueur.
        remove_from_inventory : Retire un item de l'inventaire du joueur.
    """

    def __init__(self, name, max_weight=10):
        """
        Initialise une instance de Player.

        Args :
            name (str) : Nom du joueur.
            max_weight (float, optionnel) : Poids maximum transportable. Défaut : 10 kg.
        """
        self.name = name
        self.current_room = None
        self.previous_room = None
        self.history = []
        self.inventory = []  # Utilisation d'un dictionnaire pour l'inventaire
        self.max_weight = max_weight

    def current_inventory_weight(self):
        """
        Calcule le poids total des objets dans l'inventaire du joueur.

        Returns :
            float : Le poids total des objets.
        """
        return sum(item.weight for item in self.inventory.values())

    def move(self, direction):
        """
        Permet au joueur de se déplacer dans une direction donnée.

        Args :
            direction (str) : La direction vers laquelle le joueur souhaite se déplacer.

        Returns :
            bool : True si le déplacement a réussi, False sinon.
        """
        if self.current_room is None:
            print("\nErreur : Le joueur n'est pas dans une pièce !\n")
            return False

        next_room = self.current_room.exits.get(direction)

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

        Returns :
            bool : True si le joueur est revenu à la pièce précédente, False sinon.
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

        Returns :
            str : Liste des pièces visitées.
        """
        if not self.history:
            return "Vous n'avez visité aucune pièce pour l'instant."

        history_string = "\nVous avez déjà visité les pièces suivantes :\n"
        history_string += "\n".join(f"    - {room_name}" for room_name in self.history)
        return history_string

    def add_to_inventory(self, item):
        """
        Ajoute un item à l'inventaire du joueur.

        Args :
            item (Item) : L'objet à ajouter.

        Returns :
            bool : True si l'ajout a réussi, False sinon (si le poids total est dépassé).
        """
        if self.current_inventory_weight() + item.weight > self.max_weight:
            print(f"\nVous ne pouvez pas ajouter {item.name} à votre inventaire, "
                  f"car il dépasse le poids maximum autorisé ({self.max_weight} kg).\n")
            return False

        self.inventory[item.name] = item
        print(f"\n{item.name} a été ajouté à votre inventaire.\n")
        return True

    def remove_from_inventory(self, item_name):
        """
        Retire un item de l'inventaire du joueur.

        Args :
            item_name (str) : Nom de l'objet à retirer.

        Returns :
            bool : True si l'objet a été retiré, False sinon (s'il n'est pas trouvé).
        """
        if item_name not in self.inventory:
            print(f"\n{item_name} n'est pas dans votre inventaire.\n")
            return False

        del self.inventory[item_name]
        print(f"\n{item_name} a été retiré de votre inventaire.\n")
        return True

    def get_inventory(self):
        """
        Retourne une liste descriptive des objets présents dans l'inventaire du joueur.

        Returns:
            str: Description des objets présents dans l'inventaire ou un message
                indiquant que l'inventaire est vide.
        """
        if not self.inventory:
            return "Votre inventaire est vide."

        inventory_details = "\nVotre inventaire contient les objets suivants :\n"
        inventory_details += "\n".join(
            f"    - {item_name} : {item.description} (Poids : {item.weight:.2f} kg)"
            for item_name, item in self.inventory.items()
        )
        return inventory_details
