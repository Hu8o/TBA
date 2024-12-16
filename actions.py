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

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        player = game.player
        l = len(list_of_words)

        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction_input = list_of_words[1]
        direction = game.direction_syn.get(direction_input, None)

        # Validate the direction.
        if direction is None:
            print(f"\nErreur : '{direction_input}' n'est pas une direction valide. Les directions valides sont : {', '.join(game.valide_directions)}.\n")
            return False

        # Move the player in the direction specified by the parameter.
        player.move(direction)
        print(player.get_history())

        return True


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
        Permet au joueur de revenir à la pièce précédente.

        Args:
            game (Game): Le jeu en cours.
            list_of_words (list): Les mots de la commande.
            number_of_parameters (int): Nombre de paramètres attendus.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        # Vérifier le nombre de paramètres
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Tenter de revenir en arrière
        if game.player.back():
            # Afficher l'historique après le retour en arrière
            print(game.player.get_history())
            return True
        return False


    
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

    def look(game, list_of_words, number_of_parameters):
        """
        Affiche la liste des objets présents dans la pièce actuelle du joueur.

        Args:
            game (Game): Le jeu en cours.
            list_of_words (list): La liste des mots dans la commande.
            number_of_parameters (int): Le nombre de paramètres attendu par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> look(game, ["look"], 0)
        True
        >>> look(game, ["look", "extra"], 0)
        False
        """
        l = len(list_of_words)
        
        # Vérifier si le nombre de paramètres est correct.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Obtenir la pièce actuelle du joueur.
        player = game.player
        current_room = player.current_room

        # Si le joueur n'est dans aucune pièce, afficher un message d'erreur.
        if current_room is None:
            print("\nErreur : Le joueur n'est dans aucune pièce.\n")
            return False

        # Afficher les objets présents dans la pièce.
        print(current_room.get_inventory())
        return True

    @staticmethod
    def take(player, item_name):
        """
        Permet au joueur de prendre un item dans la pièce actuelle, sous réserve de la limite de poids.

        Args:
            player (Player): Le joueur.
            item_name (str): Le nom de l'item à prendre.

        Returns:
            None
        """
        item_to_take = next((item for item in player.current_room.items if item.name == item_name),None)
        if item_to_take:
            # Vérifier la capacité de poids restante
            if player.current_inventory_weight() + item_to_take.weight > player.max_weight:
                print(f"\nErreur : Vous ne pouvez pas prendre '{item_name}' car cela dépasse votre capacité maximale de {player.max_weight} kg.")
                return

            # Ajouter l'objet à l'inventaire
            player.inventory.append(item_to_take)
            player.current_room.items.remove(item_to_take)
            print(f"\nVous avez pris l'objet '{item_name}'.")
        else:
            print(f"\nErreur : L'objet '{item_name}' n'est pas présent dans cette pièce.")

    @staticmethod
    def drop(player, item_name):
        """
        Permet au joueur de déposer un item de son inventaire dans la pièce actuelle.

        Args:
            player (Player): Le joueur qui dépose l'item.
            item_name (str): Le nom de l'item à déposer.

        Returns:
            bool: True si l'item a été déposé, False sinon.
        """
        current_room = player.current_room
        if not current_room:
            print("Vous n'êtes dans aucune pièce !")
            return False

        # Chercher l'item dans l'inventaire du joueur
        item_to_drop = None
        for item in player.inventory:
            if item.name == item_name:
                item_to_drop = item
                break

        if item_to_drop:
            # Ajouter l'item dans la pièce
            current_room.items.append(item_to_drop)
            # Retirer l'item de l'inventaire du joueur
            player.inventory.remove(item_to_drop)
            print(f"Vous avez déposé {item_to_drop.name} dans {current_room.name}.")
            return True
        else:
            print(f"{item_name} n'est pas dans votre inventaire.")
            return False
    
    @staticmethod
    def check(player):
        """
        Affiche la liste des items présents dans l'inventaire du joueur.

        Args:
            player (Player): Le joueur dont on vérifie l'inventaire.

        Returns:
            None
        """
        if not player.inventory:
            print("\nVotre inventaire est vide.")
        else:
            print("\nVotre inventaire contient :")
            for item in player.inventory:
                print(f"- {item}")