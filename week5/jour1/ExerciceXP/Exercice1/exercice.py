#Utilisation de la classe donnée par l'exercice
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

#Instanciation de 03 cats à l'aide du code fourni ci-dessus
bouli=Cat("milou",45)
bouki=Cat("toupass",32)
milou=Cat("bobi",25)
#En dehors de la classe, trouvons une fonction quit trouve le chat le plus ancien et rencoie le chat
def ChatAncien(bouli,bouki,milou):
    if(bouli.age>bouki.age and bouli.age>milou.age):
        print('Le chat le plus âge est ',bouli.name, 'et a',bouli.age,'ans')
    elif(bouki.age>bouli.age and bouki.age>milou.age):
        print('Le chat le plus âge est ',bouki.name,'et a',bouki.age,'ans')
    elif(milou.age>bouki.age and milou.age>bouli.age):
        print('Le chat le plus âge est ',milou.name,'et a',milou.age,'ans')
    else:
        print("pas de résultat")
#Impression de la chaine du chien le plus agé
ChatAncien(bouli, bouki, milou)