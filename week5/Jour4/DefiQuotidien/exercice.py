#Création de la classe Text qui prnd une chaine comme comme argument et le stocke dans un attribut
class Text:
    def __init__(self, chaine):
        self.chaine = chaine.split(" ")
#Methode de renvoie de la fréqence d'un mot dans le texte
    def freq(self, mot):
        return self.chaine.count(mot)
#Renvoie du mot le plus courant dans le texte
    def plusFreq(self):
        mot = {}
        grand = ""
        for x in self.chaine :
            if x not in mot and mot != {}:
                mot.update({x : self.freq(x)})
                if mot[grand] < mot[x]:
                    grand = x
            elif mot == {}:
                mot.update({x: self.freq(x)})
                grand = x
        return grand
#Renvoie des mots uniques dans le texte
    def unique(self):
        return list(set(self.chaine))

#Deuxième partie
#Téléchargement du fichier donné par l'exercice
    def from_file(self, nomFic):
        text = ""
        with open(nomFic, "r") as f :
            for x in f :
                text += x[0:len(x)-1]
        return text

a= Text("Un bon livre coûterait un peu mais parfois autant qu'une autant bonne chose 1 1 1 1 1 parfois  mais autant mais vraiment autant de fois hein ")
print(f"Ce mot apparait {a.freq('autant')} fois")
print(f"Le mot le plus courant est==> {a.plusFreq()}")
print(f"liste des éléments uniques==> {a.unique()}")

b = Text(a.from_file('mot.txt'))
print(f"\nCe mot apparait {b.freq('the')} fois")
print(f"Le mot le plus courant est {b.plusFreq()}")
print(f"liste des éléments unique {b.unique()}")