#Créons une classe appelée Dogavec les attributs suivants name, age, weight
class Dog():
	def __init__(self,name, age, weight):
		self.name=name
		self.age=age
		self.weight=weight
#Implémentation des methodes demandées dans la classe	
#Renvoie une chaine qui indique dog_name aboie
	def bark (self):
		Aboiement=self.name+' aboie'
		return Aboiement
#La vitesse de course du chien	
	def speed_run(self):
		vitesse=((self.weight/self.age)*10)
		return vitesse
#fight: prend un paramètre dont la valeur est une autre Doginstance, appelée autre_chien. Cette méthode renvoie une chaîne indiquant quel chien a gagné le combat. Le gagnant devrait être le chien avec le plus grand run_speed x weight .
	def fight(self,autre_chien):
		weight1=self.speed_run()*self.weight
		weight2=autre_chien.speed_run()*autre_chien.weight
		if weight1>weight2:
			print(self.name,f' puissance= {weight1} a gagné le combat contre ',autre_chien.name,f' puissance= {weight2}')
		elif(weight1==weight2):
			print(f'{self.name} and {autre_chien.name} sont égaux')
		else:
			print(f'{autre_chien.name} puissance= {weight2} a gagné le combat contre {self.name} puissance= {weight1}')
#Créons 3 chiens et faisons-les passer dans notre classe.
Rex=Dog('Rex',14,11)
Medor=Dog('Medor',17,12)
Boby=Dog('Boby',23,9)
#Affichage après passage des trois chiens dans notre classe Dog()
print(Rex.bark())
print(Rex.name,' vitesse = ',Rex.speed_run())
print(Boby.bark())
print(Boby.name,' vitesse = ',Boby.speed_run())
print(Medor.bark())
print(Medor.name,' vitesse = ',Medor.speed_run())
Rex.fight(Medor)
Rex.fight(Boby)
Rex.fight(Rex)
Medor.fight(Boby)