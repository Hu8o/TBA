class Item:
    """
    Représente un objet que le joueur peut trouver dans différents lieux de la carte.

    Attributs :
        name (str) : Le nom de l'objet.
        description (str) : Une description de l'objet.
        weight (int ou float) : Le poids de l'objet en kilogrammes.

    Méthodes :
        __init__(name, description, weight) : Initialise les attributs de l'objet.
        __str__() : Retourne une représentation textuelle de l'objet.
    """

    def __init__(self, name, description, weight):
        """
        Initialise un nouvel objet avec un nom, une description et un poids.

        Args :
            name (str) : Le nom de l'objet.
            description (str) : Une description de l'objet.
            weight (int ou float) : Le poids de l'objet en kilogrammes.
        """
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        """
        Retourne une représentation textuelle de l'objet.

        Returns :
            str : Une chaîne décrivant l'objet.
        """
        return f"{self.name} : {self.description} ({self.weight} kg)"

