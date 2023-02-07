birthday={'patrick':'1980/12/24',
           'rodrigue':'2019/02/05',
           'arlette':'2001/03/29',
           'Kevin':'2013/07/16',
           'liane':'2030/06/2001'}
name=input("entrer votre nom ==>")
birth=input("entrer votre date d'anniversaire yyyy/mm/dd ==>")
t=0
#Ajout de nouvelles données dans le dictionnaire
for cle in birthdays.keys():
    if name==cle:
        print(f"{name} is found and The corresponding birthday is found:",birthdays[name])
        t=1
        break
if t==0:
	print(f"we add {name} to the list with birthday date {birth}")
	birthdays[name]=birth
	print(birthdays)
