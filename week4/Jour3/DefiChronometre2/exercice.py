mot = input("Entrez une phrase : ")
mot = mot.split(" ")
phrase = ""
for x in range(len(mot)-1,-1,-1) :
    phrase += mot[x] + " "
    print(x)
print(phrase)