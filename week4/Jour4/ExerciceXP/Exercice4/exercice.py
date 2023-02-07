#Création d'une fonction qui accepte un nombre entre 1 et 100 et génère un autre nombre aléatoirement entre 1 et 100.
import random
numb = 0
def Alea_number(numb):
    Alea = random.randint(1,100)
    if(Alea == numb):
        print("Félicitations, vous avez trouvé le secret")
    else : 
        print(f"Désolé! vous n'avez pas trouvé le bon nombre. Le bon nombre est {Alea} et pas {numb}")
while (numb < 1 or numb > 100):
    print("Vous devez entrer un nombre entre 1 et 100")
    numb=int(input("Svp entrer un nombre entre 1 à 100==>"))
Alea_number(numb)