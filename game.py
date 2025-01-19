# Description: Game class
"Projet TBA 2025"
# Imports standards
import tkinter as tk

# Imports tiers
from PIL import Image, ImageTk

# Imports locaux
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character

class Game:
    """
    Classe principale représentant la logique du jeu, y compris l'initialisation, 
    la configuration et le traitement des commandes.
    """

    def __init__(self):
        """
        Initialise l'état du jeu.
        """
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None

    def setup(self):
        """
        Configure le monde du jeu, les directions valides, les commandes disponibles, 
        et les raccourcis de directions.
        """
        # Directions valides dans le jeu
        self.valide_directions = ["N", "E", "S", "O", "NE", "NO", "SE", "SO", "D", "U"]

        # Raccourcis et synonymes pour les directions
        self.direction_syn = {
            "N": "N", "NORD": "N", "Nord": "N", "nord": "N", "n": "N",
            "E": "E", "EST": "E", "Est": "E", "est": "E", "e": "E",
            "S": "S", "SUD": "S", "Sud": "S", "sud": "S", "s": "S",
            "O": "O", "OUEST": "O", "Ouest": "O", "ouest": "O", "o": "O",
            "D": "D", "d": "D", "U": "U", "u": "U",
            "NE": "NE", "Nord-Est": "NE", "nord-est": "NE", "NORD-EST": "NE", "ne": "NE",
            "NO": "NO", "no": "NO", "nord-ouest": "NO", "NORD-OUEST": "NO", "Nord-Ouest": "NO",
            "SE": "SE", "se": "SE", "Sud-Est": "SE", "sud-est": "SE", "SUD-EST": "SE",
            "SO": "SO", "so": "SO", "sud-ouest": "SO", "SUD-OUEST": "SO", "Sud-Ouest": "SO"
        }

        # Configuration des commandes du jeu
        self.commands = {
            "go": Command("go", " - Déplace le joueur dans une direction.", Actions.go, 1),
            "quit": Command("quit", " - Quitte le jeu.", Actions.quit, 0),
            "help": Command("help", " - Affiche la liste des commandes disponibles.", Actions.help, 0),
            "history": Command("history", " - Affiche l'historique des pièces visitées.", Actions.history, 0),
            "back": Command("back", " - Retourne à la pièce précédente.", Actions.back, 0),
            "take": Command("take", " - Permet de prendre un item dans la pièce actuelle.", Actions.take, 1),
            "look": Command("look", " - Permet de voir les items dans la pièce actuelle.", Actions.look, 1),
            "drop": Command("drop", " - Permet de déposer un item dans la pièce actuelle.", Actions.drop, 1),
            "check": Command("check", " - Permet de regarder le contenu de son sac.", Actions.check, 0),
            "talk": Command("talk", " - Permet de parler à un personnage dans la pièce actuelle.", Actions.talk, 1)
        }


        # Setup des pièces du jeu
        # Chaque pièce est créée avec un nom et une description, puis ajoutée à la liste des pièces.

        # Pièce : Forêt
        forest = Room(
            "Forest", 
            "Dans une forêt dense. Vous entendez une biche à travers les fougères! Lancez votre attaque !!"
        )
        self.rooms.append(forest)

        # Pièce : Tanière
        cave = Room(
            "Cave", 
            "Dans la tanière profonde et sombre de la mère de votre louvetau. "
            "Vous devez passer à l'action pour le faire évoluer."
        )
        self.rooms.append(cave)

        # Pièce : Rivière large
        river = Room(
            "River", 
            "Face à une large rivière profonde. Votre loup sera-t-il capable de la traverser ?"
        )
        self.rooms.append(river)

        # Pièce : Petite rivière
        small_river = Room(
            "Small_River", 
            "Face à une petite rivière peu profonde. Votre loup sera-t-il capable de la traverser ?"
        )
        self.rooms.append(small_river)

        # Pièce : Arbre
        tree = Room(
            "Tree", 
            "Face à un large chêne. Votre loup a aperçu un dindon à son sommet."
        )
        self.rooms.append(tree)

        # Pièce : Grotte de l'ours
        bear_cave = Room(
            "Bear_cave", 
            "Face à une large grotte sombre et odorante. C'est la grotte du plus gros ours du coin ! "
            "Votre loup sera-t-il capable de voler la nourriture de l'ours ?"
        )
        self.rooms.append(bear_cave)

        # Pièce : Prairie
        prairie = Room(
            "Prairie", 
            "Face à un beau troupeau de moutons. C'est peut-être l'occasion d'attaquer ! "
            "Mais attention, un chien monte la garde et peut tuer votre petit loup."
        )
        self.rooms.append(prairie)

        # Pièce : Montagne
        mountain = Room(
            "Mountain", 
            "Au milieu d'une montagne entourée de randonneurs. Votre petit loup ne doit pas être vu !"
        )
        self.rooms.append(mountain)

        # Pièce : Grotte personnelle
        personnal_cave = Room(
            "Personnal_Cave", 
            "Votre espace personnel. Un refuge sûr pour réfléchir et se préparer."
        )
        self.rooms.append(personnal_cave)

        # Pièce : Grande grotte
        great_cave = Room(
            "Great_Cave", 
            "Face au loup le plus sage de tout le secteur. Il est là pour vous donner des conseils "
            "pour évoluer et gagner en compétence."
        )
        self.rooms.append(great_cave)

        # Pièces : Zones humaines
        human1 = Room("Human1", "Les humains vous attaquent !!")
        self.rooms.append(human1)
        human2 = Room("Human2", "Les humains vous attaquent !!")
        self.rooms.append(human2)
        human3 = Room("Human3", "Les humains vous attaquent !!")
        self.rooms.append(human3)

        # Pièces : Zones sûres
        safe1 = Room("Safe1", "Vous n'êtes pas passé loin des hommes !")
        self.rooms.append(safe1)
        safe2 = Room("Safe2", "Vous n'êtes pas passé loin des hommes !")
        self.rooms.append(safe2)

        # Pièces : Zones festives
        festin1 = Room("Festin1", "Au bon endroit pour vous régaler !")
        self.rooms.append(festin1)
        festin2 = Room("Festin2", "Au bon endroit pour vous régaler !")
        self.rooms.append(festin2)
        festin3 = Room("Festin3", "Au bon endroit pour vous régaler !")
        self.rooms.append(festin3)
        festin4 = Room("Festin4", "Au bon endroit pour vous régaler !")
        self.rooms.append(festin4)
        festin5 = Room("Festin5", "Au bon endroit pour vous régaler !")
        self.rooms.append(festin5)


        # Création des sorties pour chaque pièce
        # Chaque pièce est liée à d'autres pièces via des directions cardinales ou spécifiques.

        # Forest
        forest.exits = {
            "N": None,
            "E": cave,
            "S": None,
            "O": None,
            "NO": None,
            "NE": None,
            "SO": festin2,
            "SE": None,
            "U": None,
            "D": None
        }

        # Cave
        cave.exits = {
            "N": mountain,
            "E": prairie,
            "S": bear_cave,
            "O": forest,
            "NO": river,
            "NE": small_river,
            "SO": None,
            "SE": None,
            "U": tree,
            "D": great_cave
        }

        # Prairie
        prairie.exits = {
            "N": None,
            "E": None,
            "S": festin3,
            "O": cave,
            "NO": None,
            "NE": None,
            "SO": None,
            "SE": None,
            "U": None,
            "D": None
        }

        # Mountain
        mountain.exits = {
            "N": None,
            "E": None,
            "S": cave,
            "O": None,
            "NO": human1,
            "NE": safe1,
            "SO": None,
            "SE": None,
            "U": None,
            "D": None
        }

        # Bear Cave
        bear_cave.exits = {
            "N": cave,
            "E": None,
            "S": None,
            "O": None,
            "NO": None,
            "NE": None,
            "SO": None,
            "SE": None,
            "U": None,
            "D": None
        }

        # Tree
        tree.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": None,
            "NO": None,
            "NE": None,
            "SO": None,
            "SE": None,
            "U": None,
            "D": cave
        }

        # Small River
        small_river.exits = {
            "N": festin5,
            "E": None,
            "S": None,
            "O": None,
            "NO": None,
            "NE": None,
            "SO": cave,
            "SE": None,
            "U": None,
            "D": None
        }

        # River
        river.exits = {
            "N": festin1,
            "E": None,
            "S": None,
            "O": None,
            "NO": None,
            "NE": None,
            "SO": forest,
            "SE": cave,
            "U": None,
            "D": None
        }

        # Great Cave
        great_cave.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": None,
            "NO": None,
            "NE": None,
            "SO": None,
            "SE": None,
            "U": cave,
            "D": None
        }

        # Human1
        human1.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": None,
            "NO": None,
            "NE": None,
            "SO": None,
            "SE": mountain,
            "U": None,
            "D": None
        }

        # Human2
        human2.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": None,
            "NO": None,
            "NE": None,
            "SO": safe1,
            "SE": None,
            "U": None,
            "D": None
        }

        # Human3
        human3.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": None,
            "NO": None,
            "NE": None,
            "SO": None,
            "SE": safe2,
            "U": None,
            "D": None
        }

        # Safe1
        safe1.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": None,
            "NO": safe2,
            "NE": human2,
            "SO": mountain,
            "SE": None,
            "U": None,
            "D": None
        }

        # Safe2
        safe2.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": None,
            "NO": human3,
            "NE": festin4,
            "SO": None,
            "SE": safe1,
            "U": None,
            "D": None
        }

        # Festin1
        festin1.exits = {
            "N": None,
            "E": None,
            "S": river,
            "O": None,
            "NO": None,
            "NE": None,
            "SO": None,
            "SE": None,
            "U": None,
            "D": None
        }

        # Festin2
        festin2.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": None,
            "NO": None,
            "NE": forest,
            "SO": None,
            "SE": None,
            "U": None,
            "D": None
        }

        # Festin3
        festin3.exits = {
            "N": prairie,
            "E": None,
            "S": None,
            "O": None,
            "NO": None,
            "NE": None,
            "SO": None,
            "SE": None,
            "U": None,
            "D": None
        }

        # Festin4
        festin4.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": None,
            "NO": None,
            "NE": None,
            "SO": safe2,
            "SE": None,
            "U": None,
            "D": None
        }

        # Festin5
        festin5.exits = {
            "N": None,
            "E": None,
            "S": small_river,
            "O": None,
            "NO": None,
            "NE": None,
            "SO": None,
            "SE": None,
            "U": None,
            "D": None
        }


        # Initialisation du joueur et définition de la pièce de départ
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = cave

        # Initialisation des items
        badge_tortue = Item(
            "Badge tortue", 
            "Votre loup a débloqué sa peur de l'eau", 
            0.1
        )
        small_river.add_item(badge_tortue)

        viande2 = Item(
            "Viande", 
            "Votre loup vient d'attraper un beau pigeon !", 
            1
        )
        safe2.add_item(viande2)

        badge_ecureuil = Item(
            "Badge écureuil", 
            "Votre loup a débloqué la compétence de grimper aux arbres !", 
            1
        )
        tree.add_item(badge_ecureuil)

        badge_dauphin = Item(
            "Badge dauphin", 
            "Votre loup a débloqué la nage comme compétence", 
            0.1
        )
        river.add_item(badge_dauphin)

        badge_tueur = Item(
            "Badge tueur", 
            "Votre loup a débloqué la compétence prédateur", 
            0.1
        )
        festin3.add_item(badge_tueur)

        badge_phantom = Item(
            "Badge phantom", 
            "Votre loup a débloqué la discrétion comme compétence", 
            0.1
        )
        safe2.add_item(badge_phantom)

        viande3 = Item(
            "Viande", 
            "Votre loup a trouvé une carcasse de cerf !", 
            0.1
        )
        festin2.add_item(viande3)

        viande5 = Item(
            "Viande", 
            "Votre loup a tué un mouton !", 
            0.1
        )
        festin3.add_item(viande5)

        viande4 = Item(
            "Viande", 
            "Votre loup a trouvé un beau poisson échoué sur le rivage !", 
            0.1
        )
        festin5.add_item(viande4)


        # Liste de tous les items dans le jeu
        self.all_items = [viande3,viande2,viande4,viande5,badge_dauphin,badge_ecureuil,badge_phantom,badge_tueur]  # Autres items peuvent être ajoutés ici.

        # Création des personnages
        la_louve = Character(
            name="La Louve",
            description="Une louve majestueuse et protectrice qui veille sur la tanière.",
            current_room=None,  # Défini comme "cave" plus tard
            msgs=[
                "Mon petit, tu viens de naître, tu dois faire tes preuves face au grand loup pour faire partie des nôtres."
            ]
        )

        le_grand_loup = Character(
            name="Le Grand Loup",
            description="Un loup imposant avec des yeux perçants et une allure féroce.",
            current_room=great_cave,
            msgs=[
                "Le Grand Loup grogne doucement, montrant ses crocs.",
                "Ses yeux brillent dans la pénombre, vous observant attentivement.",
                "Il se tient immobile, un hurlement résonne au loin."
            ]
        )

        hibou = Character(
            name="Hibou",
            description="Un bel oiseau pouvant indiquer où sont les Hommes. Communiquez avec lui !",
            current_room=great_cave,
            msgs=["Il y a un groupe de randonneurs au nord-ouest. Prenez la direction nord-est pour les éviter !"]
        )

        chouette = Character(
            name="Chouette",
            description="Un bel oiseau pouvant aussi indiquer où sont les Hommes. Communiquez avec elle !",
            current_room=great_cave,
            msgs=["Il y a un groupe de randonneurs au nord-est. Prenez la direction nord-ouest pour les éviter !"]
        )

        renard = Character(
            name="Renard",
            description="Un roi de la discrétion qui peut vous aider !",
            current_room=great_cave,
            msgs=["Attention ! J'ai aperçu des Hommes au nord-ouest ! Prenez vite la direction nord-est !"]
        )

        # Ajout des personnages aux pièces correspondantes
        great_cave.add_character(le_grand_loup)
        cave.add_character(la_louve)
        mountain.add_character(hibou)
        safe1.add_character(chouette)
        safe2.add_character(renard)


    def play(self):
        """
        Initialise et exécute la boucle principale du jeu.
        """
        self.setup()
        self.print_welcome()
        while not self.finished:
            user_input = input("> ").strip()
            if user_input:
                self.process_command(user_input)

    def process_command(self, command_string):
        """
        Traite la commande entrée par le joueur.

        Args:
            command_string (str): La commande saisie par le joueur.
        """
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]

        if command_word not in self.commands:
            print(f"\nCommande '{command_word}' non reconnue. "
                "Entrez 'help' pour voir la liste des commandes disponibles.\n")
            return

        command = self.commands[command_word]
        command.action(self, list_of_words, command.number_of_parameters)

        # Vérification de la victoire après chaque commande
        if self.check_victory():
            self.finished = True

    def print_welcome(self):
        """
        Affiche le message de bienvenue au début du jeu.
        """
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())

    def display_victory_image_fullscreen(self):
        """
        Affiche une image de victoire en plein écran pour célébrer la réussite du joueur.
        """
        try:
            img = Image.open("victory_image.png")
            img = img.resize((1920, 1080), Image.ANTIALIAS)

            root = tk.Tk()
            root.title("Victoire !")
            root.attributes('-fullscreen', True)

            tk_img = ImageTk.PhotoImage(img)
            label = tk.Label(root, image=tk_img)
            label.pack(expand=True)

            def close_window(event=None):
                root.destroy()

            root.bind("<Escape>", close_window)
            label.bind("<Button-1>", close_window)

            root.mainloop()
        except FileNotFoundError:
            print("\nImage introuvable. Assurez-vous que 'victory_image.png' est dans le répertoire du jeu.")
        except Exception as error:
            print("\nImpossible d'afficher l'image de victoire en plein écran.")
            print(f"Erreur : {error}")

    def check_victory(self):
        """
        Vérifie si tous les items du jeu sont dans la pièce 'Great_cave'.

        Returns:
            bool: True si tous les items sont dans 'Great_cave', False sinon.
        """


        # Recherche de 'great_cave'
        great_cave = next((room for room in self.rooms if room.name.lower() == "great_cave"), None)

        if not great_cave:
            print("Erreur : La pièce 'Great_cave' est introuvable.")
            return False

        # Vérification des items manquants
        missing_items = [item for item in self.all_items if item not in great_cave.items]

        if missing_items:
            print("\033[31m\nItems manquants dans 'Great_cave' :\033[0m")
            for item in missing_items:
                print(f"\033[33m- {item.name}\033[0m")
            return False

        # Victoire
        self.display_victory_image_fullscreen()
        print("\033[32m\nFélicitations ! Vous avez ramené tous les items dans la 'Great_cave'. Vous avez gagné !\033[0m")
        return True




def main():
    "activation"
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()