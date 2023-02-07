class Farm():
	def __init__(self,farm):	
		self.nom=farm
		self.animals_list=[]
		self.num=[]
		print(self.nom +"'s farm")
	def add_animal(self,nom,nb=1):
		if nom in self.animals_list:
			self.num[self.animals_list.index(nom)]=self.num[self.animals_list.index(nom)]+nb
		else:
			self.animals_list.append(nom)
			self.num.append(nb)

	def get_info(self):
		for i in self.animals_list:
			print(i,' : ',self.num[self.animals_list.index(i)])
		print("\n \tE-I-E-I-0!")
		
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat',12)
macdonald.get_info()