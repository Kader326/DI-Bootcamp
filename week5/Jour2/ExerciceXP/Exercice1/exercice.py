class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
#Créons une autre race de chat nommée Siamesequi hérite de la Catclasse.
class Siamese(Cat):
	def sing(self, sounds):
		return f'{sounds}'

#Créons une liste appelée all_cats, qui contient trois instances de chat : un bengal, un chartreux et un siamois.
toto=Bengal('totoli',12)
titi=Chartreux('titila',11)
lala=Siamese('lalato',10)
all_cats=[toto,titi,lala]
#Ces trois chats sont les animaux de compagnie de Sara. Créons une variable appelée sara_petsdont la valeur est une instance de la Petclasse et transmettez la variable all_catsà la nouvelle instance.
sara_pets=Pets(all_cats)
#Promenons tous les chats, utilisez la walkméthode.
sara_pets.walk()
