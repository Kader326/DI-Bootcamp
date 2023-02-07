#création de la fonction get_words_from_file
def get_words_from_file():
    with open('mot.txt') as f:
        mot = []
        for line in f:
            mot.append(line[0:len(line)-1])
    return mot
#Création de la fonction get_random_sentence qui prend un seul paramètre length
def get_random_sentence(length=6):
    import random
    sentence = ""
    mots = get_words_from_file()
    for x in range (0,length):
        sentence += mots[random.randint(0,len(mots))] + ' '
    return sentence
#Création d'une phrase aves les mots obtenus de façon aléatoire
mot = get_random_sentence().lower()
print(mot)

#Création de la fonction main() qui exécute un certain nombre de tâches
def main():
  #Message expliquant ce que fait le programme
    print("\nCe programme génère une phrase de faàon aléatoire.\nVous devez juste donner le nombre de mots que vous souhaitez retrouver dans votre phrase")
    length = int(input('Entrez la taille de votre phrase mais entre 2 et 20 ==> '))
    if length >= 2 and length <= 20:
        print(get_random_sentence(length))
main()