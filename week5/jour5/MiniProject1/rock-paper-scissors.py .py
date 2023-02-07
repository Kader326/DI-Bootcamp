from game import Game
#Création de trois fonctions
#Affichage d'un menu simple de choix de possibles
def get_user_menu_choice():
    choix = input("Svp pour jouer à une nouvelle partie tapez 1\npour afficher les scores tapez 2\npour quitter tapez 'x'==> ")
    return choix
#Impression des résultats des parties jouées
def print_results(results):
    print("\tlistes des jeux passés\n")
    for x in results:
        print(f"{x} --- Nombre : {results[x]}")
#La fonction principale, la fonction main()
def main():
    results = {
        "win": 0,
        "draw": 0,
        "loss": 0
    }
    #Affichage repeté du menu
    while True:
        a = get_user_menu_choice()
        if a == "x":
            print_results(results)
            return 0
        elif a == "1":
            jeu = Game()
            result = jeu.play()
            results.update({result: results[result] + 1})
        elif a == "2":
            print_results(results)
        print("")
main()