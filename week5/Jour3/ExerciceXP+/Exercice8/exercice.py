#calcul de l'âfe que quelqu'un aurait sur jupiter en fonction de son âge donné en secondes
def age_sur_jupiter():
    ageS = 1000000000
    print(f"Vous avez sur terre : {ageS/31557600} ans.")
    print(f"Vous avez sur Mercure  : {ageS/(31557600 * 0.2408467)} ans.")
    print(f"Vous avez sur Vénus   : {ageS/(31557600 * 0.61519726)} ans.")
    print(f"Vous avez sur Mars    : {ageS/(31557600 * 1.8808158)} ans.")
    print(f"Vous avez sur Jupiter     : {ageS/(31557600 * 11.862615)} ans.")
    print(f"Vous avez sur Mars    : {ageS/(31557600 * 29.447498)} ans.")
    print(f"Vous avez sur Uranus    : {ageS/(31557600 * 84.016846)} ans.")
    print(f"Vous avez sur Neptune     : {ageS/(31557600 * 164.79132)} ans.")

age_sur_jupiter()
