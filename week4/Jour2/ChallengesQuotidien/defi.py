new_chaine=""
chaine=input("entrer une chaine de lettres Svp==>")
for i in chaine:
    if new_chaine == '' or i != new_chaine[len(new_chaine)-1]:
        new_chaine += i
print(new_chaine)
