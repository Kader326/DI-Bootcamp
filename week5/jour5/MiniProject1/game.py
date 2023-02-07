#Création de la classe Game avec quatres modules
class Game:
    #Methode de demande du choix de l'utilisateur
    def get_user_item(self):
        while True:
            choix = input(" Svp taper 1 pour pierre; 2 pour papier ou 3 pour ciseaux. Quel est votre choix==> ")
            if choix == "1":
                choix = "pierre"
            elif choix == "2":
                choix = "papier"
            elif choix == "3":
                choix = "ciseaux"
            if choix == "pierre" or choix == "papier" or choix == "ciseaux":
                return choix.lower()
#Selection de façon aléatoire du choix de l'ordinateur
    def get_computer_item(self):
        import random
        computer_choice = ["pierre", "papier", "ciseaux"]
        return random.choice(computer_choice)
#Determinons le résultat du jeu
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "Match nul!"
        elif user_item == "pierre" and computer_item == "ciseaux":
            return "Victoire!"
        elif user_item == "ciseaux" and computer_item == "papier":
            return "Victoire"
        elif user_item == "papier" and computer_item == "pierre":
            return "Victoire"
        else:
            return "Défaite"

    def play(self):
        utilisateur = self.get_user_item()
        ordinateur = self.get_computer_item()
        result = self.get_game_result(utilisateur, ordinateur)
        print(f"Voici votre choix==> {utilisateur} et voici celui de l'ordinateur {ordinateur}.\nResutats : {result}")
        return result