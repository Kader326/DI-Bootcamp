#Création d'un nouveau fichier Python puis importons notre class Dog()
from Exercice_XP import Dog
from random import randint
#Création d'une classe nommée PetDog qui hérite de Dog et ajoit d'un attribut trained
class PetDog(Dog):
	def __init__(self,name,age,weight):
		super().__init__(name,age,weight)
		self.trained=False
#Ajout d'autres methodes
#train imprine la sortie de bark et bascule trained en true
	def train(self):
		self.trained=True
		print(self.bark())
#prend un paramètre qui est les noms d'autres chiens	
	def play(self,*args):
		print(f'{args} all play together')
#Condition de dressage d'un chien
	def do_a_trick(self):
		if self.trained==True:
			Dressage=[self.name+' does a barrel roll', self.name+' stands on his back legs', self.name+' shakes your hand', self.name+' plays dead']
			val=randint(0,3)
			print(Dressage[val])
		else:
			print(f'{self.name} is not trained ')

Rex=PetDog('Rex',12,13)
Medor=PetDog('ron',22,20)
Boby=PetDog('Boby',14,25)

Rex.train()
Medor.train()
Rex.fight(Boby)
Rex.play(Rex.name,Medor.name,Boby.name)
Rex.do_a_trick()
Boby.do_a_trick()
Medor.do_a_trick()
