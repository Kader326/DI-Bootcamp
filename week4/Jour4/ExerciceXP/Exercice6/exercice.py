#Utilisation de la liste donnée par l'exercice
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
#Passons la liste à une fonction qui imprime le nom de chaque magicien
def show_magicians(names):
    for i in names:
        print(i)
show_magicians(magician_names)
#Écrivons une fonction appelée make_great()qui modifie la liste des magiciens en ajoutant la phrase "the Great"au nom de chaque magicien.
def make_great(names):
    for i in names:
        print("the great", i)
make_great(magician_names)