#Création d'une classe appelée dog
class Dog:
#Dans cette classe, créons une __init__méthode qui prend deux paramètres : nameet height. Cette fonction instancie deux attributs, dont les valeurs sont les paramètres.
	def __init__(self,nom,poids):
		self.nom = nom
		self.poids = poids
#Créons une méthode appelée barkqui imprime la chaîne suivante " <dog_name>va woof!"
	def bark(self) :
		print(f"{self.nom} va woof!")
#Mise en pratique
	def jump(self) :
		print(f"{self.nom} saute {self.poids*2} cm")
#le chien de David
chien_david=Dog('Rex',50)
print(f'le chien de David s appelle {chien_david.nom} et son poids est {davids_dog.poids}')
chien_david.bark()
chien_david.jump()
#le chien de Sarah
chien_sarah=Dog('Teacup',20)
print(f'le chien de David s appelle {chien_sarah.nom} et son poids est {sarahs_dog.poids}')
chien_sarah.bark()
chien_sarah.jump()
#Instruction de comparaison des chiens
if chien_sarah.height > chien_david.height:
	print(f"{chien_sarah.nom} est le plus grand ")
else:
	print(f"{chien_david.nom} est le plus grand ")
