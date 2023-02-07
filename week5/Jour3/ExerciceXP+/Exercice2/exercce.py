#Création une fonction acceptant un nombre entre 1 et 100 puis le lancement d'un nombre aléatoire entre 1 et 100
def alea (num1) :
    import random as r
    if num1 in range(0,101):
        if num1 == r.randint(0,100):
            print("Super")
alea(9)
