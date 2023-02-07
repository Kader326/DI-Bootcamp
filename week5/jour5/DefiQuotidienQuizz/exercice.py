#Partie 1 : Quizz 
#Répondons aux questions.
# Qu'est-ce qu'une classe ?
#C'est un moyen de reunir des fonctionnalités en créant plusieurs methodes que nous pouvons rappeler dans d'autres codes

# Qu'est-ce qu'une instance ?
#Une instance en programmation oreintée objet est un objet avec un comportement et un état.

# Qu'est-ce que l'encapsulation ?
#L'encapsulation en programmation orientée objet est un principe qui consiste à protéger ou à cacher des données de certains objets

# Qu'est-ce que l'abstraction ?
#L'abstraction, c'est le fait de ne pouvoir instanciée une classe

# Qu'est-ce que l'héritage ?
#C'est la possibilité donnée à une classe d'avoir les attributs d'une autre classe

# Qu'est-ce que l'héritage multiple ?
#Possibilité donnée à une classe d'avoir les attributs de deux ou de plusieurs autres classes

# Qu'est-ce que le polymorphisme ?
#En programmation orientée objet, le polymorphisme est la capacité donnée à une variable, à une fonction ou à un objet à prendre plusieurs formes

# Qu'est-ce que l'ordre de résolution de méthode ou MRO ?
#C'est la manière dont python va chercher les méthodes et les attributs d'une classe


# Partie 2 : Créer Une Classe De Jeu De Cartes.
#Réalisation de la classe Card qui doit avoir une couleur et une variable
class Card:
    def __init__(self,couleur,valeur):
        self.couleur = couleur
        self.valeur = valeur

class Deck:
    #Methode shuffle pour s'assurer que le jeu de cartes contient 52 cartes puis les ré-organise de façon aléatoire
    def shuffle(self,tab):
        import random
        tab1 = []
        taille = 51
        for x in range(0,52):
            tab1.append(tab.pop(random.randint(0,taille)))
            taille -= 1
        return tab1
#Attribution de couleurs et de valeurs aux cartes
    def genCard(self,couleur):
        cardTab = []
        cardTab.append(Card(couleur, "A"))
        cardTab.append(Card(couleur, "J"))
        cardTab.append(Card(couleur, "Q"))
        cardTab.append(Card(couleur, "K"))
        for i in range(2,11):
            cardTab.append(Card(couleur, i))
        return cardTab
#Distribution d'une seule carte du jeu et la retire du paquet
    def deal(self,tab):
        return tab.pop()

a = Deck()
pack = a.genCard("Hearts")
pack += a.genCard("Diamonds")
pack += a.genCard("Clubs")
pack += a.genCard("Spades")

for x in pack:
    print(x.couleur,x.valeur)
print()

pack = a.shuffle(pack)

for x in pack:
    print(x.couleur,x.valeur)
print()

user = a.deal(pack)

for x in pack:
    print(x.couleur,x.valeur)
print()

