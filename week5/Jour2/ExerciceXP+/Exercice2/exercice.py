#Création de la classe et ajout d'autres clés
class TheIncredibles(Family):
	def __init__(self,name):
		super().__init__(name)
		i=0
		for j in self.members:
			if i==0:
				dictionnaire={'power': 'fly','incredible_name':'MikeFly'}
				j.update(dictionnaire)
				i=i+1
			else:
				dico={'power': 'read minds','incredible_name':'SuperWoman'}
				j.update(dico)
#Fonction use_power
#cette méthode doit imprimer le pouvoir d'un membre uniquement s'il a plus de 18 ans. Si ce n'est pas le cas, soulevez une exception (recherchez des exceptions) indiquant qu'ils n'ont pas plus de 18 ans.
	def use_power(self,name):
		v=self.is_18(name)
		if v==True:
			for i in self.members:
				for j in i.keys():
					if i[j]==name:
						print(f'{i[j]} a un pouvoir qui est {i["power"]}')
		else:
			raise Exception(f'{name} n as pas 18 ans donc tu ne peux pas utiliser ton pouvoir')
#Methode incredible_presentation
	def incredible_presentation(self):
		self.family_presentation()
		for i in self.members:
			print(f'{i["name"]} avec {i["incredible_name"]} a une puissance {i["power"]} \n')
toto=TheIncredibles('Coopers')
toto.incredible_presentation()
toto.born(name='Baby Jack ',age=0,gender='masculin',is_child=True,power='inconnue d abord',incredible_name='inconnue')
toto.incredible_presentation()
