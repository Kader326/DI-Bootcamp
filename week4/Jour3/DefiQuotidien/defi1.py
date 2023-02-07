#Demande d'un mot à l'utilisateur
# chaine = input("Svp veillez entrer un mot==>")

# Véraification que les letttres sont des chaines
import re
pattern = re.compile(r"(^[a-zA-Z]+$)+")
cond = pattern.fullmatch(chaine)
if cond ==None:
    print("retapper un mot svp")
else :

      liste = {}
      fin=len(chaine)
      for i in range(0,fin) :
              if chaine[i] in liste :
                  liste[chaine[i]].append(i)
              else :
                  liste[chaine[i]]=[i]
      print(liste)