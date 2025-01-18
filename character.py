import random

class Character:
    """
    Représente un personnage non joueur (PNJ) dans le jeu.

    Attributs:
        name (str): Le nom du personnage.
        description (str): La description du personnage.
        current_room (Room): La pièce où se trouve le personnage.
        msgs (list): Une liste de messages associés au personnage.
    """

    def __init__(self, name, description, current_room=None, msgs=None):
        """
        Initialise un personnage avec un nom, une description, une pièce actuelle et une liste de messages.

        Args:
            name (str): Le nom du personnage.
            description (str): La description du personnage.
            current_room (Room, optional): La pièce initiale où se trouve le personnage. Par défaut à None.
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs if msgs is not None else [] 

    def add_message(self, message):
        """
        Ajoute un message à la liste des messages du personnage.

        Args:
            message (str): Le message à ajouter.
        """
        self.msgs.append(message)

    def get_messages(self):
        """
        Retourne les messages du personnage sous forme de liste.

        Returns:
            list: Les messages associés au personnage.
        """
        return self.msgs

    def interact(self):
        """
        Affiche les messages du personnage lorsque le joueur interagit avec lui.
        Si aucun message n'est disponible, affiche un message par défaut.
        """
        if not self.msgs:
            print(f"{self.name} n'a rien à dire pour le moment.")
        else:
            print(f"{self.name} dit:")
            for msg in self.msgs:
                print(f"    - {msg}")

    def move_to_room(self, new_room):
        """
        Déplace le personnage dans une nouvelle pièce.

        Args:
            new_room (Room): La nouvelle pièce où déplacer le personnage.
        """
        self.current_room = new_room

    def get_location(self):
        """
        Retourne la pièce actuelle du personnage.

        Returns:
            Room: La pièce actuelle du personnage.
        """
        return self.current_room

    def describe(self):
        """
        Affiche la description du personnage.
        """
        print(f"{self.name}: {self.description}")


    def get_random_message(self):
        """
        Retourne un message aléatoire parmi les messages du personnage.

        Returns:
            str: Un message aléatoire.
        """
        if not self.msgs:
            return "Le personnage reste silencieux."
        return random.choice(self.msgs)
