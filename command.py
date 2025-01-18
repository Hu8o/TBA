# Ce fichier contient la classe Command.

class Command:
    """
    Représente une commande dans le jeu, composée d'un mot de commande, 
    d'une description d'aide, d'une action et du nombre de paramètres requis.

    Attributs :
        command_word (str) : Le mot utilisé pour invoquer la commande.
        help_string (str) : Une description de l'action de la commande.
        action (function) : La fonction exécutée lorsque la commande est invoquée.
        number_of_parameters (int) : Le nombre de paramètres requis par la commande.

    Méthodes :
        __init__ : Initialise une instance de Command avec les attributs donnés.
        __str__ : Retourne une représentation textuelle de la commande.

    Exemples :
        >>> from actions import go
        >>> commande = Command("aller", "Permet de se déplacer.", go, 1)
        >>> commande.command_word
        'aller'
        >>> commande.help_string
        'Permet de se déplacer.'
        >>> type(commande.action)
        <class 'function'>
        >>> commande.number_of_parameters
        1
    """

    def __init__(self, command_word, help_string, action, number_of_parameters):
        """
        Initialise une instance de la classe Command avec les attributs spécifiés.

        Args :
            command_word (str) : Le mot de commande.
            help_string (str) : Une description de la commande.
            action (function) : La fonction exécutée lors de l'invocation.
            number_of_parameters (int) : Le nombre de paramètres attendus.
        """
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters

    def __str__(self):
        """
        Retourne une représentation textuelle de la commande.

        Returns :
            str : Le mot de commande suivi de sa description d'aide.
        """
        return f"{self.command_word} - {self.help_string}"
