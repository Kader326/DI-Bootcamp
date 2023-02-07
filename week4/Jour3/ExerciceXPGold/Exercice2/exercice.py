birthday={'patrick':'1980/12/24',
           'rodrigue':'2019/02/05',
           'arlette':'2001/03/29',
           'Kevin':'2013/07/16',
           'liane':'2030/06/2001'}
           #Impression de tous les noms
print("Tous les noms ==>",birthdays)
t=0
#demande du nom de la personne
name=input("entre votre nom ==>")
for cle in birthdays.keys():
    if name==cle:
        t=1
        print("The birthday of ",cle)
        print(birthdays[name])
if t==0:
	#Si la personne n'est pas dans le dictionnaire impression d'un message
 print("Désolé! nous ne connaissons pas votre date d'anniversaire",name)
