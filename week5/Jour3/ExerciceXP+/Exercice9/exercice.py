#installation du module faker et utilisation dans notre code
users = []#création d'une liste vide appelée users
#Fonction ajoutant de nouveaux dictionnaires
def modFaker(users):

    from faker import Faker
    faker = Faker()
    langue = ['fr','en','aa','af']
    lang = str(faker.sentence(ext_word_list = langue)).split(" ")
    users.append({'nom': faker.name(),'adresse': faker.address(), 'code_langue': lang[0]})

modFaker(users)
modFaker(users)
modFaker(users)
modFaker(users)
print(users)
