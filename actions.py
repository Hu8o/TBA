# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    @staticmethod
    def go(game, params, num_params):
        """
        Permet au joueur de se déplacer dans une direction, avec gestion des conditions de victoire/défaite
        et de l'historique des pièces visitées.

        Args:
            game (Game): L'instance du jeu.
            params (list): La commande entrée par le joueur, avec la direction en deuxième mot.
            num_params (int): Le nombre attendu de paramètres pour la commande.

        Returns:
            None
        """
        if len(params) < 2:
            print("\nVous devez spécifier une direction.")
            return

        direction = params[1].upper()
        current_room = game.player.current_room

        if direction not in current_room.exits or current_room.exits[direction] is None:
            print("\nVous ne pouvez pas aller dans cette direction.")
            return

        # Récupère la pièce suivante
        next_room = current_room.exits[direction]

        # Ajoute la pièce actuelle à l'historique avant tout déplacement
        if not hasattr(game, 'room_history'):
            game.room_history = []
        game.room_history.append(current_room)

        # Vérifie si le joueur entre dans "River" sans le "Badge tortue"
        if next_room.name == "River" and not any(item.name == "Badge tortue" for item in game.player.inventory):
            print("\nVous avez essayé de traverser la rivière sans le 'Badge tortue'. Vous avez perdu !")
            game.finished = True
            return

        # Vérifie si le joueur entre dans "Bear_cave" (défaite automatique)
        if next_room.name == "Bear_cave":
            print("\nVous avez osé entrer dans la tanière de l'ours. Votre louveteau ne fait pas le poids face à un tel adversaire.")
            print("Vous avez perdu !")
            game.finished = True
            return

        # Déplace le joueur dans la nouvelle pièce
        game.player.current_room = next_room
        print(f"\nVous êtes maintenant dans : {next_room.name}.")
        print(next_room.get_long_description())



    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def back(game, list_of_words, number_of_parameters):
        """
    Action pour revenir à la pièce précédente.

    Args:
        game (Game): Instance du jeu.
        list_of_words (list): Liste des mots de la commande (non utilisé ici).
        number_of_parameters (int): Nombre de paramètres (non utilisé ici).
    """
        if game.player.back():
        # Si le joueur a pu revenir, on affiche une description de la pièce actuelle.
            print(game.player.current_room.get_long_description())
        else:
        # Si le joueur ne peut pas revenir en arrière.
            print("Vous ne pouvez pas revenir en arrière.")


    
    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def history(game, list_of_words, number_of_parameters):
        
        l = len(list_of_words)
        # Vérifier le nombre de paramètres
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Afficher l'historique du joueur
        print(game.player.get_history())
        return True

    def look(game, list_of_words=None, number_of_parameters=None):
        """
    Affiche les détails de la pièce actuelle, y compris les objets et les personnages présents.

    Args:
        game (Game): Le jeu en cours.
        list_of_words (list, optional): La liste des mots dans la commande.
        number_of_parameters (int, optional): Le nombre de paramètres attendu par la commande.

    Returns:
        bool: True si la commande a été exécutée avec succès, False sinon.
    """
    # Validation des arguments (si nécessaire).
        if list_of_words and len(list_of_words) > 1:
            print("La commande 'look' ne prend pas de paramètres.")
            return False

    # Reste du code pour afficher les détails de la pièce.
        player = game.player
        current_room = player.current_room

        if current_room is None:
            print("\nErreur : Vous n'êtes dans aucune pièce.\n")
            return False

        print(current_room.get_long_description())

        inventory = current_room.get_inventory()
        """if inventory:
            print("\nObjets présents dans la pièce :\n")
            for item in inventory:
                print(f"    - {item.name}: {item.description} ({item.weight} kg)")
        else:
            print("\nIl n'y a aucun objet dans cette pièce.")"""

        if current_room.characters:
            print("\nPersonnages présents dans la pièce :\n")
            for character in current_room.characters:
                print(f"    - {character.name}: {character.description}")
        else :
            print("\nIl n'y a aucun personnage dans cette pièce.\n")

        if current_room.items:
            print("\nItems présents dans la pièce :\n")
            for item in current_room.items:
                print(f"    - {item.name}: {item.description}")
        else :
            print("\nIl n'y a aucun item dans cette pièce.\n")
        
        return True


    @staticmethod
    def drop(game, params, num_params):
        """
    Permet au joueur de déposer un item de son inventaire dans la pièce actuelle.

    Args:
        game (Game): L'instance du jeu.
        params (list): La liste des mots de la commande, où le deuxième mot est l'item à déposer.
        num_params (int): Le nombre attendu de paramètres pour la commande.

    Returns:
        None
    """
        if len(params) < 2:
            print("\nVous devez spécifier quel item vous voulez déposer.")
            return

        item_name = params[1]  # Récupère le nom de l'item
        current_room = game.player.current_room

    # Recherche l'item dans l'inventaire du joueur
        item_to_drop = None
        for item in game.player.inventory:
            if item.name.lower() == item_name.lower():
                item_to_drop = item
                break

        if item_to_drop is None:
            print(f"\nVous ne possédez pas l'item '{item_name}' dans votre inventaire.")
            return

    # Supprimer l'item de l'inventaire et l'ajouter à la pièce actuelle
        game.player.inventory.remove(item_to_drop)
        current_room.add_item(item_to_drop)
        print(f"\nVous avez déposé '{item_to_drop.name}' dans la pièce actuelle.")

    
    @staticmethod
    def check(game, list_of_words, num_params):
    # Vérifie le contenu de l'inventaire du joueur
        if not game.player.inventory:
            print("\nVotre inventaire est vide.")
        else:
            print("\nContenu de votre inventaire :")
            for item in game.player.inventory:
                print(f"- {item.name}: {item.description}")

    @staticmethod
    def take(game, list_of_words, num_params):
        """
    Permet au joueur de prendre un item dans la pièce actuelle.

    Args:
        game (Game): L'objet représentant le jeu.
        list_of_words (list): Les mots de la commande entrée par le joueur.
        num_params (int): Nombre de paramètres requis pour cette commande.

    Returns:
        None
    """
    # Vérifie si le joueur a spécifié un nom d'item
        if len(list_of_words) < 2:
            print("\nVous devez spécifier quel item vous voulez prendre.")
            return
    
    # Récupère le nom de l'item spécifié
        item_name = " ".join(list_of_words[1:])  # Gère les noms multi-mots
        current_room = game.player.current_room

    # Vérifie si l'item est dans la pièce actuelle
        item = current_room.get_item_by_name(item_name)
        if item:
        # Ajoute l'item à l'inventaire du joueur
            game.player.inventory.append(item)
        # Retire l'item de la pièce
            current_room.items.remove(item)
            print(f"\nVous avez pris l'item '{item.name}'.")
        else:
            print(f"\nL'item '{item_name}' n'est pas dans cette pièce.")

    @staticmethod
    def talk(game, params, num_params):
        """
        Permet au joueur de parler à un personnage dans la pièce actuelle.

        Args:
            game (Game): L'instance du jeu.
            params (list): Les mots de la commande, où le deuxième mot est le nom du personnage.
            num_params (int): Le nombre attendu de paramètres pour la commande.

        Returns:
            None
        """
        if len(params) < 2:
            print("\nVous devez spécifier à qui vous voulez parler.")
            return

        character_name = " ".join(params[1:]).lower()  # Nom insensible à la casse
        current_room = game.player.current_room

        # Vérifie si le personnage est présent dans la pièce
        character = current_room.get_character_by_name(character_name)
        if character:
            print(f"\n{character.name} vous dit : \"{character.get_random_message()}\"")
        else:
            print(f"\nIl n'y a pas de personnage nommé '{character_name}' dans cette pièce.")
