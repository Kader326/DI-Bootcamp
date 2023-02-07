#Création d'une classe qui représente un cercle simple
class Circle:
    def __init__(self, radius):
        self.radius = radius
#Calcul de l'aire du cercle
    def aire(self):
        import math
        return math.pi * self.radius
#Impression du cercle avec quelque chose de sympa
    def __str__(self):
        return "Géniaaaaaal"
#Addition de deux cercles
    def __add__(self, other):
        return self.radius + other.radius
#Comparaison de deux cercles pour voir lequel est le plus grand
    def comp(self, other):
        if self.radius < other.radius :
            return f"Le cercle avec pour rayon {other.radius} est le plus grand."
        elif self.radius > other.radius :
            return f"Le cercle avec pour rayon {self.radius} est le plus grand."
        return "Egalité"

    def egal(self, other):
        if self.radius == other.radius:
            return True
        return False
#Rangement dans une liste et les trier
    def trie(self,*args):
        tab = []
        for x in args:
            tab.append(x)
        for i in range(0,len(tab)):
            tmp = tab[i]
            j=i-1
            while j>=0 and tab[j].radius > tmp.radius:
                tab[j+1] = tab[j]
                j=j-1
            tab[j+1] = tmp
            print(tab)
        return tab

boite = Circle(7)
toto  = Circle(45)
tata  = Circle(15)
lili  = Circle(115)
titi  = Circle(511)
lala  = Circle(50)
print(boite)
print(boite.aire())
print(boite.comp(toto))
print(boite.egal(toto))
tab = boite.trie(toto,tata,lili,titi,lala)
for x in tab :
    print(x.radius)