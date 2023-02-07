import random
def get_random_temp():
    return random.randrange(-10,40)
Test_fonction = [get_random_temp() for i in range(5)]
print(Test_fonction)

#Création d'une fonction appelée main().
def main():
    temperature = get_random_temp()
    print(f"La temperature actuelle est {temperature}°C")
#Ajout de fonctionnalités
    if(temperature < 0):
        print("Brrr, c'est glacial ! Portez des couches supplémentaires aujourd'hui")
    elif (temperature > 0 and temperature <= 16):
        print("Assez froid ! N'oubliez pas votre manteau")
    elif (temperature > 16 and temperature <= 23):
        print("Le temps est sexy")
    elif (temperature > 24 and temperature <= 32):
        print("Il fera un peu chaud")
    elif (temperature > 30 and temperature <= 40):
        print("Il fera très chaud")
main()
def get_random_temp(saison):
    if saison == "été":
        return random.randrange(-10,16)
    if saison == "automne":
        return random.randrange(16,23)
    if saison == "hiver":
        return random.randrange(24,32)
    if saison == "printemps":
        return random.randrange(33,40)
    else:
        return random.randrange(-10,40)
def main():
    saison = input("Entrer une saison svp==> ")
    temperature = get_random_temp(saison)
    if(temperature < 0):
        print("Brrr, c'est glacial ! Portez des couches supplémentaires aujourd'hui")
    elif (temperature > 0 and temperature <= 16):
        print("Assez froid ! N'oubliez pas votre manteau")
    elif (temperature > 16 and temperature <= 23):
        print("Le temps est sexy")
    elif (temperature > 24 and temperature <= 32):
        print("Il fera un peu chaud")
    elif (temperature > 30 and temperature <= 40):
        print("Il fera très chaud")
main()