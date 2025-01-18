
"""Description du module des actions. 
Le module des actions contient les fonctions qui sont appelées lorsqu'une commande est exécutée.
Chaque fonction prend 3 paramètres :
- game : l'objet représentant le jeu
- list_of_words : la liste des mots dans la commande
- number_of_parameters : le nombre de paramètres attendus par la commande
Les fonctions retournent True si la commande a été exécutée avec succès, False sinon.
Les fonctions affichent un message d'erreur si le nombre de paramètres est incorrect.
Le message d'erreur varie en fonction du nombre de paramètres attendus par la commande."""


# Le message d'erreur est stocké dans les variables MSG0 et MSG1 et est formaté avec la 
# variable command_word, le premier mot de la commande.
# La variable MSG0 est utilisée lorsque la commande ne prend aucun paramètre.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# La variable MSG1 est utilisée lorsque la commande prend 1 seul paramètre.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"


class Actions:
    """
    Cette classe gère toutes les actions du jeu, telles que se déplacer, prendre des objets,
    quitter le jeu, etc. Chaque méthode définit une action possible pour le joueur.
    """

    @staticmethod
    def go(game, params, num_params):
        """
        Permet au joueur de se déplacer dans une direction.

        Cette méthode permet au joueur de spécifier une direction pour se déplacer dans
        la pièce actuelle. Elle vérifie si la direction est valide et si le joueur peut
        se déplacer dans cette direction. Si des conditions particulières sont remplies
        (comme l'absence d'un objet nécessaire pour traverser une rivière), le joueur
        perd la partie.

        Args:
            game (Game): L'instance du jeu.
            params (list): La commande entrée par le joueur, où la direction se trouve en deuxième position.
            num_params (int): Le nombre attendu de paramètres pour la commande.

        Returns:
            None
        """
        if len(params) < 2:
            print("\nVous devez spécifier une direction.")
            return

        direction = params[1].upper()
        current_room = game.player.current_room

        # Vérifie si la direction est valide
        if direction not in current_room.exits or current_room.exits[direction] is None:
            print("\nVous ne pouvez pas aller dans cette direction.")
            return

        # Récupère la pièce suivante
        next_room = current_room.exits[direction]

        # Gère l'historique des pièces visitées
        if not hasattr(game, 'room_history'):
            game.room_history = []
        game.room_history.append(current_room)

        if not hasattr(game, 'unique_room_history'):
            game.unique_room_history = []
        if current_room not in game.unique_room_history:
            game.unique_room_history.append(current_room)

        # Vérification des règles de défaite
        if next_room.name == "River" and not any(item.name == "Badge tortue" for item in game.player.inventory):
            print("\nVous avez essayé de traverser la rivière sans le 'Badge tortue'. Vous avez perdu !")
            game.finished = True
            return

        if next_room.name == "Bear_cave":
            print("\nVous avez osé entrer dans la tanière de l'ours. Votre louveteau ne fait pas le poids face à un tel adversaire.")
            print("Vous avez perdu !")
            game.finished = True
            return

        if next_room.name in ["human1", "human2", "human3"]:
            print("\nVous avez été capturé et tué.")
            print("Vous avez perdu !")
            game.finished = True
            return

        # Déplace le joueur dans la nouvelle pièce
        game.player.current_room = next_room
        print(f"\nVous êtes maintenant dans : {next_room.name}.")
        print(next_room.get_long_description())

    @staticmethod
    def quit(game, list_of_words, num_params):
        """
        Quitte le jeu.

        Args:
            game (Game): L'instance du jeu.
            list_of_words (list): La liste des mots de la commande.
            num_params (int): Le nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.

        Examples:
            >>> from game import Game
            >>> game = Game()
            >>> game.setup()
            >>> Actions.quit(game, ["quit"], 0)
            True
            >>> Actions.quit(game, ["quit", "N"], 0)
            False
        """
        # Vérifie si le nombre de paramètres est incorrect
        if len(list_of_words) != num_params + 1:
            print(f"Erreur : La commande '{list_of_words[0]}' ne prend pas de paramètres supplémentaires.")
            return False

        # Termine le jeu
        player = game.player
        print(f"\nMerci {player.name} d'avoir joué. Au revoir.\n")
        game.finished = True
        return True


    @staticmethod
    def back(game, _, num_params):
        """
        Permet au joueur de revenir à la pièce précédente.

        Args:
            game (Game): L'instance du jeu.
            _ (list): La commande entrée par le joueur (pas utilisée ici).
            num_params (int): Le nombre attendu de paramètres pour la commande.

        Returns:
            None
        """
        if not hasattr(game, 'room_history') or not game.room_history:
            print("\nVous ne pouvez pas revenir en arrière, aucun déplacement précédent.")
            return

        # Revenir à la dernière pièce visitée
        last_room = game.room_history.pop()  # Retire la dernière pièce
        game.player.current_room = last_room
        print(f"\nVous êtes revenu dans : {last_room.name}.")
        print(last_room.get_long_description())




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

    @staticmethod
    def history(game, params, num_params):
        """
        Affiche l'historique des pièces visitées par le joueur sans répétition.

        Args:
            game (Game): L'instance du jeu.
            params (list): La commande entrée par le joueur (pas utilisée ici).
            num_params (int): Le nombre attendu de paramètres pour la commande.

        Returns:
            None
        """
        if not hasattr(game, 'unique_room_history') or not game.unique_room_history:
            print("\nAucune pièce visitée pour le moment.")
            return

        print("\nHistorique des pièces visitées (sans répétition) :")
        for idx, room in enumerate(game.unique_room_history, start=1):
            print(f"{idx}. {room.name} - {room.description}")


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

        current_room = game.player.current_room
        print(current_room.get_long_description())

        if "Bear_cave" in [exit.name for exit in current_room.exits.values() if exit]:
            print("\nUn avertissement résonne dans votre esprit : \"Ne vous approchez pas de la tanière de l'ours, c'est trop dangereux !\"")

        return True


    @staticmethod
    def drop(game, params, num_params):
        """
        Permet au joueur de déposer un item de son inventaire dans la pièce actuelle.

        Cette méthode permet au joueur de spécifier un item à déposer de son inventaire dans
        la pièce actuelle. Si l'item est présent dans l'inventaire du joueur, il est retiré de
        l'inventaire et ajouté à la pièce.

        Args:
            game (Game): L'instance du jeu qui permet d'accéder à l'état du jeu, à l'inventaire du
                         joueur et à la pièce actuelle.
            params (list): La liste des mots de la commande, où le deuxième mot est l'item à déposer.
            num_params (int): Le nombre attendu de paramètres pour la commande. Utilisé pour vérifier
                               que la commande a été correctement entrée.

        Returns:
            None

        Notes:
            - Si le joueur ne spécifie pas l'item, un message d'erreur est affiché.
            - Si l'item n'est pas trouvé dans l'inventaire du joueur, un message d'erreur est affiché.
            - Si l'item est trouvé, il est retiré de l'inventaire et ajouté à la pièce.
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

        # Supprime l'item de l'inventaire et l'ajoute à la pièce actuelle
        game.player.inventory.remove(item_to_drop)
        current_room.add_item(item_to_drop)
        print(f"\nVous avez déposé '{item_to_drop.name}' dans la pièce actuelle.")

    @staticmethod
    def take(game, list_of_words, num_params):
        """
        Permet au joueur de prendre un item dans la pièce actuelle.

        Cette méthode permet au joueur de spécifier un item à prendre dans la pièce actuelle,
        d'ajouter cet item à l'inventaire du joueur et de le retirer de la pièce.

        Args:
            game (Game): L'objet représentant le jeu. Permet d'accéder à l'état du jeu, 
                         à la pièce actuelle du joueur et à son inventaire.
            list_of_words (list): Les mots de la commande entrée par le joueur. Le deuxième
                                  mot doit être le nom de l'item à prendre.
            num_params (int): Le nombre de paramètres attendus pour cette commande. Permet 
                               de vérifier si la commande a été entrée correctement avec 
                               les paramètres nécessaires.

        Returns:
            None

        Notes:
            - Si le joueur ne spécifie pas un item, un message d'erreur est affiché.
            - Si l'item est trouvé dans la pièce, il est ajouté à l'inventaire du joueur 
              et retiré de la pièce.
            - Si l'item n'est pas trouvé, un message d'erreur est affiché.
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

    def check(self):
        """
        Vérifie et affiche le contenu de l'inventaire du joueur.

        Returns:
            None
        """
        if not self.player.inventory:
            print("\nVotre inventaire est vide.\n")
        else:
            print("\nVoici le contenu de votre inventaire :")
            for item_name, item in self.player.inventory.items():
                print(f"  - {item_name} : {item.description} (Poids : {item.weight} kg)")
