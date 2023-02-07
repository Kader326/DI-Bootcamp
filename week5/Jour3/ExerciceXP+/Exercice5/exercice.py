#Création d'une fonction qui affiche le temps restant jusqu'au 1er janvier.
def timeRest():
    import datetime
    janv = "01/01/2023"
    janv = datetime.datetime.strptime(janv, "%d/%m/%Y")
    rest = janv-datetime.datetime.now()
    rest1= str(rest)
    print(f"il reste {rest.days} et {rest1[len(rest1)-14:len(rest1)-7]} heures")

timeRest()