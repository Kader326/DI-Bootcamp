fruits=input("Saisir vos fruits préféres:")
fruitsPreferes=[] #liste vide pour récupérer les fruits saisis par l'utilisateur 
fruitsPreferes.append(fruits) #Stocke les fruits préférés dans une liste
print(fruitsPreferes) #Affiche les fruits 
for i in fruitsPreferes:
    choix=input("Entrer le nom de n'importe quel fruit:")
    if choix in i: #Pour vérifier si l'entrée de l'utilisateur se trouve dans la liste si oui affiche
        print("vous avez choisi l'un de vos fruits préféres!Prendre plaisir")   
    else: #Dans le cas contraire affiche autrement
        print("vous avez choisi un nouveau fruit. J'espère que tu apprécies")
