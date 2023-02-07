#Génération d'une chaine aléatoire de longueur 5
import random as r
import string

chaine = "".join([r.choice(string.ascii_letters) for i in range(0,5)])

print(chaine)