#Fonction affichant la date du jour
def dateJour():
    import datetime
    print(datetime.datetime.now())
#Elle doit aussi afficher le temps restant jusqu'aux prochaines vacances à venir et impression de quelles vacances il s'agit
    vac = "25/12/2022"
    vac = datetime.datetime.strptime(vac, "%d/%m/%Y")
    rest = vac-datetime.datetime.now()
    rest1 = str(rest)
    print(f"il reste {rest.days} et {rest1[len(rest1)-14:len(rest1)-7]} heures pour la noël")

dateJour()
