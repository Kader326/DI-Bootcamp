#La classe pagination doit accepter deux paramètres
class Pagination:
#item qui est par défaut une liste et le nombre de page 10 par défaut
    def __init__(self, items = [], pageSize = 10):
        self.items = items
        self.pageSize = int(pageSize)
        self.current = 0
#Impléméntation des méthodes de la classe
#getVisibleItems qui renvoie une liste elements en fonction du numéro de page
    def getVisibleItems(self):
            return self.items[self.current:len(self.items)]
#mise en place de différentes methodes pour parcourir les pages telles que:
    def prevPage(self):
        self.current -= self.pageSize

    def nextPage(self):
        self.current += self.pageSize

    def firstPage(self):
        self.current = 0

    def lastPage(self):
        if len(self.items)%self.pageSize == 0 :
            self.current = len(self.items)-self.pageSize
        else :
            self.current = len(self.items)-len(self.items)%self.pageSize

    def goToPage(self,pageNum):
        self.current = pageNum
#Récupération de l'exemple donné dand l'exercice
alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
#Différentes tests des methodes implémentées
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
p.prevPage()
print(p.getVisibleItems())
p.lastPage()
print(p.getVisibleItems())
p.firstPage()
print(p.getVisibleItems())