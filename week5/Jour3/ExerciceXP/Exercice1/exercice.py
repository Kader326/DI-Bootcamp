class Info:
    def __init__(self):
#Ecriture d'un programme qui imprime les résultats des fonctions intégrées puthon
        print(abs(7.5))
        print(int("15"))
        print(input('Appuyer sur ||Entrer||'))

    def __doc__(self):
        return "Le programme imprime les résultats des fonctions: abd(), int() et input()"

information = Info()
print(information.__doc__())