#Créez une fonction qui accepte une date de naissance comme argument (dans le format de votre choix), puis affiche un message indiquant combien de minutes l'utilisateur a vécu dans sa vie.
def vie():
    import datetime
    anniv = input("Entrez votre date d'anniversaire en respectant le format DD/MM/YYYY : ")
    anniv = datetime.datetime.strptime(anniv, "%d/%m/%Y")
    minute = datetime.datetime.now() - anniv
    print(f"Vous avez vécu pendant {int(minute.total_seconds()/60)} minutes.")

vie()