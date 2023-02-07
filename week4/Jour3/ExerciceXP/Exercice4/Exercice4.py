#utilisation de la liste donnée par l'exercice
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
#Analyse des résultats
#Il y'aura erreur d'écution car des variables ne seront pas réconnues par le système
#Utilisation d'une boucle for pour recréer le 1er résultat. Astuce : ne codez pas les numéros en dur.
numéros = [num for num,val in enumerate(users)]
disney_users_A = dict(zip(users,numéros))
print(disney_users_A)
#Utilisation d'une boucle for pour recréer le 2ème résultat. Astuce : ne codez pas les numéros en dur.
disney_users_B = dict(zip(numéros,users))
print(disney_users_B)
#Utilisation d'une méthode pour recréer le 3ème résultat. Astuce : Le 3ème résultat est trié par ordre alphabétique
disney_users_C = dict(zip(sorted(users),numéros))
print(disney_users_C)
#Recréez uniquement le 1er résultat pour :
#Les caractères dont les noms contiennent la lettre "i"
new_users = []
for x in users :
    if 'i' in x :
        new_users.append(x)
print(dict(zip(new_users,numéros)))
#Les caractères, dont les noms commencent par la lettre « m » ou « p ».
new_users1 = []
for x in users :
    if x[0].lower() =='m' or x[0].lower() == 'p' :
        new_users1.append(x)
print(dict(zip(new_users1,numéros)))