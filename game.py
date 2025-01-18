# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character

class Game:

    # Constructor
    def __init__(self):
        
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None

        
    
    # Setup the game
    def setup(self):

        self.valide_directions = ["N", "E", "S", "O","NE","NO","SE","SO","D","U"]

        self.direction_syn = {
            "N": "N", "NORD": "N", "Nord": "N", "nord": "N", "n":"N",
            "E": "E", "EST": "E", "Est": "E", "est": "E","e":"E",
            "S": "S", "SUD": "S", "Sud": "S", "sud": "S","s":"S",
            "O": "O", "OUEST": "O", "Ouest": "O", "ouest": "O","o":"O",
            "D":"D","d":"D",
            "U":"U","u":"U",
            "NE":"NE","Nord-Est":"NE","nord-est":"NE","NORD-EST":"NE","ne":"NE",
            "NO":"NO","no":"NO","nord-ouest":"NO","NORD-OUEST":"NO","no":"NO","Nord-Ouest":"NO",
            "SE":"SE","se":"SE","Sud-Est":"SE","sud-est":"SE","SUD-EST":"SE",
            "SO":"SO","so":"SO","sud-ouest":"SO","SUD-OUEST":"SO","Sud-Ouest":"SO"
        }

        # Setup commands
        self.commands = {
            "go": Command("go", " - Déplace le joueur dans une direction.", Actions.go, 1),
            "quit": Command("quit", " - Quitte le jeu.", Actions.quit, 0),
            "help": Command("help", " - Affiche la liste des commandes disponibles.", Actions.help, 0),
            "history": Command("history", " - Affiche l'historique des pièces visitées.", Actions.history, 0),
            "back": Command("back", " - Retourne à la pièce précédente.", Actions.back, 0),
            "take": Command("take", "Permet de prendre un item dans la pièce actuelle.", Actions.take, 1),
            "look": Command("look", "Pemret de voir les items dans la pièce actuelle.",Actions.look,1),
            "drop": Command("drop", "Permet de déposer un item dans la pièce actuelle.", Actions.drop, 1),
            "check":Command("check","Pemret de regarder le contenu de son sac", Actions.check,0),
            "talk": Command("talk", "Permet de parler à un personnage dans la pièce actuelle.", Actions.talk, 1)
}           
       
        # Setup rooms

        forest = Room("Forest", "dans une forêt dense. Vous entendez une biche à travers les fougères! Lancez votre attaque !!")
        self.rooms.append(forest)
        cave = Room("Cave", "dans la tanière profonde et sombre de la mère de votre louvetau. Vous devez passer à l'action pour le faire évoluer.")
        self.rooms.append(cave)
        river = Room("River", "face à une large rivière profonde. Votre loup sera t il capable de la traverser.")
        self.rooms.append(river)
        small_river = Room("Small_River", "face à une petite rivière peu profonde. Votre loup sera t il capable de la traverser.")
        self.rooms.append(small_river)
        tree = Room("tree", "face à une large chêne. Votre loup a aperçu un dindon à son sommet.")
        self.rooms.append(tree)
        bear_cave = Room("Bear_cave", "face à une large grottesombre et odorante. C'est la grotte du plus gros ours du coin ! Votre loup sera t il capable de voler la nourriture de l'ours ?")
        self.rooms.append(bear_cave)
        prairie = Room("prairie", "face à un beau troupeaux de moutons. C'est peut-être l'occasion d'attaquer ! Mais attention à vous un chien monte la garde et peut tuer votre petit loup ")
        self.rooms.append(prairie)
        mountain = Room("mountain", "au milieu d'une montagne entouré de randonneurs. Votre petit loup ne doit pas être vu!")
        self.rooms.append(mountain)
        personnal_cave = Room("personnal_cave", " ")
        self.rooms.append(personnal_cave)
        great_cave = Room("great_cave", "face au loup le plus sage de tout le secteur. Il est la pour vous donnez les conseils popur évoluer et gagner en compétence")
        self.rooms.append(great_cave)
        human1 = Room("human1", "Les humains vous attanquent !!")
        self.rooms.append(human1)
        human2 = Room("human2", "Les humains vous attanquent !!")
        self.rooms.append(human2)
        human3 = Room("human3", "Les humains vous attanquent !!")
        self.rooms.append(human3)
        safe1 = Room("safe1", "Vous n'êtes pas passé loin des hommes !")
        self.rooms.append(safe1)
        safe2 = Room("safe2", "Vous n'êtes pas passé loin des hommes !")
        self.rooms.append(safe2)
        festin1 = Room("festin1", "Vous avez de quoi avoir des conseils du grand loup")
        self.rooms.append(festin1)
        festin2 = Room("festin2", "Vous avez de quoi avoir des conseils du grand loup")
        self.rooms.append(festin2)
        festin3 = Room("festin3", "Vous avez de quoi avoir des conseils du grand loup")
        self.rooms.append(festin3)
        festin4 = Room("festin4", "Vous avez de quoi avoir des conseils du grand loup")
        self.rooms.append(festin4)
        festin5 = Room("festin5", "Vous avez de quoi avoir des conseils du grand loup")
        self.rooms.append(festin5)
        # Create exits for rooms

        """"forest.exits = {"N" : cave, "E" : tower, "S" : castle, "O" : None}
        tower.exits = {"N" : cottage, "E" : None, "S" : None, "O" : None}
        cave.exits = {"N" : None, "E" : cottage, "S" : forest, "O" : None}
        cottage.exits = {"N" : None, "E" : None, "S" : tower, "O" : cave}
        swamp.exits = {"N" : tower, "E" : None, "S" : None, "O" : castle}
        castle.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None}"""

        forest.exits={"N":None, "E":cave, "S":None,"O":None,"NO":None,"NE":None,"SO":festin2,"SE":None,"U":None,"D":None}
        cave.exits={"N":mountain,"E":prairie,"S":bear_cave,"O":forest,"NO":river ,"NE":small_river,"SO":None,"SE":None,"U":tree,"D":great_cave}
        prairie.exits={"N":None,"E":None,"S":festin3,"O":cave,"NO":None,"NE":None,"SO":None,"SE":None,"U":None,"D":None}
        mountain.exits={"N":None,"E":None,"S":cave,"O":None,"NO":human1,"NE":safe1,"SO":None,"SE":None,"U":None,"D":None}
        bear_cave.exits={"N":cave,"E":None,"S":None,"O":None,"NO":None,"NE":None,"SO":None,"SE":None,"U":None,"D":None}
        tree.exits={"N":None,"E":None,"S":None,"O":None,"NO":None,"NE":None,"SO":None,"SE":None,"U":None,"D":cave}
        small_river.exits={"N":festin5,"E":None,"S":None,"O":None,"NO":None,"NE":None,"SO":cave,"SE":None,"U":None,"D":None}
        river.exits={"N":festin1,"E":None,"S":None,"O":None,"NO":None,"NE":None,"SO":forest,"SE":cave,"U":None,"D":None}
        #personnal_cave.exits={"N" : , "E" : , "S" : , "O" : ,"NO": ,"NE":,"SO":,"SE":,"U":,"D":}
        great_cave.exits={"N":None,"E":None,"S":None,"O":None,"NO":None,"NE":None,"SO":None,"SE":None,"U":cave,"D":None}
        human1.exits={"N":None,"E":None,"S":None,"O":None,"NO":None,"NE":None,"SO":None,"SE":mountain,"U":None,"D":None}
        human2.exits={"N":None,"E":None,"S":None,"O":None,"NO":None,"NE":None,"SO":safe1,"SE":None,"U":None,"D":None}
        human3.exits={"N":None,"E":None,"S":None,"O":None,"NO":None,"NE":None,"SO":None,"SE":safe2,"U":None,"D":None}
        safe1.exits={"N":None,"E":None,"S":None,"O":None,"NO":safe2,"NE":human2,"SO":mountain,"SE":None,"U":None,"D":None}
        safe2.exits={"N":None,"E":None,"S":None,"O":None,"NO":human3,"NE":festin4,"SO":None,"SE":safe1,"U":None,"D":None}
        festin1.exits={"N":None,"E":None,"S":river,"O":None,"NO":None,"NE":None,"SO":None,"SE":None,"U":None,"D":None}
        festin2.exits={"N":None,"E":None,"S":None,"O":None,"NO":None,"NE":forest,"SO":None,"SE":None,"U":None,"D":None}
        festin3.exits={"N":prairie,"E":None, "S":None,"O":None,"NO":None,"NE":None,"SO":None,"SE":None,"U":None,"D":None}
        festin4.exits={"N":None,"E":None, "S":None,"O":None,"NO":None,"NE":None,"SO":safe2,"SE":None,"U":None,"D":None}
        festin5.exits={"N":None,"E":None, "S":small_river,"O":None,"NO":None,"NE":None,"SO":None,"SE":None,"U":None,"D":None}


    # Modifications dans la méthode setup()

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = cave

    # Setup items

        viande1 = Item("Viande 1kg", "Votre loup a trouvé un beau morceau de viande", 0.1)
        prairie.add_item(viande1)
        badge_tortue = Item("Badge tortue", "Votre loup a débloqué sa peur de l'eau", 0.1)
        small_river.add_item(badge_tortue)
        viande2 = Item("Viande 1kg", "Votre loup vient d'attraper un beau pigeon !", 1)
        safe2.add_item(viande2)
        badge_ecureuil = Item("Badge écureuil", "Votre loup a débloqué la compétence de grimper aux arbres!", 1)
        tree.add_item(badge_ecureuil)
        badge_dauphin = Item("Badge dauphin", "Votre loup a débloqué la nage comme compétence", 0.1)
        river.add_item(badge_dauphin)
        badge_tueur = Item("Badge tueur", "Votre loup a débloqué la compétence prédateur", 0.1)
        prairie.add_item(badge_tueur)
        badge_phantom = Item("Badge phantom", "Votre loup a débloqué la discrétion comme compétence", 0.1)
        safe2.add_item(badge_phantom)
        viande3 = Item("viande", "Votre loup a trouvé une carcasse de cerf !", 0.1)
        festin2.add_item(viande3)

        # Liste de tous les items dans le jeu
        self.all_items = [viande1, badge_tortue, viande2, badge_ecureuil, badge_dauphin, badge_tueur, badge_phantom]
   
    # 2. Création du personnage nommé "Le Grand Loup"
        la_louve = Character(
        name="La Louve",
        description="Une louve majestueuse et protectrice qui veille sur la tanière.",
        current_room=None,  # Sera défini comme "cave"
        msgs=[
            "Mon petit, tu viens de naître, tu dois faire tes preuves face au grand loup pour faire partie des nôtres."
        ]
    )
        
        
        le_grand_loup = Character(
        name="Le Grand Loup",
        description="Un loup imposant avec des yeux perçants et une allure féroce.",
        current_room=great_cave,
        msgs=["Le Grand Loup grogne doucement, montrant ses crocs.","Ses yeux brillent dans la pénombre, vous observant attentivement.","Il se tient immobile, un hurlement résonne au loin."])

    # 3. Ajouter le personnage à la pièce
        great_cave.add_character(le_grand_loup)
        cave.add_character(la_louve)

    # Play the game

    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string):
        if not command_string.strip():
            return

        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]

        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

            # Vérification de la victoire après chaque commande
            if self.check_victory():
                print("\nFélicitations ! Vous avez ramené tous les items dans la 'Great_cave'. Vous avez gagné !")
                self.finished = True

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    
    def check_victory(self):
        great_cave = next((room for room in self.rooms if room.name == "great_cave"), None)
        if not great_cave:
            print("Erreur : La pièce 'Great_cave' est introuvable.")
            return False

        missing_items = [item for item in self.all_items if item not in great_cave.items]

        if missing_items:
            print("\nItems manquants dans 'Great_cave' :")
            for item in missing_items:
                print(f"- {item.name}")
            return False

        return True

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
