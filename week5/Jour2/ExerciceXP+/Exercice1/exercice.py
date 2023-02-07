#Créons une classe appelée Family et implémentez les attributs suivants :
#Les menbres sont la liste d'un dictionnaire donné dans l'exercice
class Family():
	def __init__(self,name):
		self.members=[ 
						{'name':'Michael','age':35,'gender':'Male','is_child':False},
						{'name':'Sarah','age':32,'gender':'Female','is_child':False}
					]
		self.last_name=name
#Implémentataion des methodes demandées par l'exercice	
#Ajout d'un enfant à la liste des menbres et felicitations
	def born(self,**kwargs):
		dictionnaire={}
		for arg,k in kwargs.items():
			dictionnaire[arg]=k
		self.members.append(dictionnaire)
		print(f'Toutes mes félicitaions à votre famille {self.last_name} pour {kwargs["name"]}')
#Prise du nom d'un menbre de la famille et retour de true ou false selon l'age 	
	def is_18(self,name):
		for i in self.members:	
			for j in i.keys():
				if i[j]==name:
					if i['age']>=18:
						print(f'{name} is over 18')
						return True
					else:
						print(f'{name} is under 18')
						return False
#Impression du nom de famille et des prénoms de tous les menbres de la famille
	def family_presentation(self):
		print(f'\t Family {self.last_name}')
		for i in self.members: 
			print( i['name'])