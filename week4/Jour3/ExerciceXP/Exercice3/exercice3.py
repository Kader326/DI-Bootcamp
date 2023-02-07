
# #Création d'undictionnaire appelé brand dont la valeur correspond aux informations de la première partie
brand = {
     "name": 'Zara',
     "creation_date": 1975,
     "creator_name": ['Amancio', 'Ortega', 'Gaona'],
     "type_of_clothes": ['men', 'women', 'children', 'home'],
     "international_competitors": ['Gap', 'H&M', 'Benetton'],
     "number_stores": 7000,
     "major_color": 
    {
         "France": 'blue',
        "Spain": 'red',
         "US": ['pink', 'green']
     }
 }

 #Modification du nombre de magasins à 2
brand["number_stores"] = 2
 #impression d'une phrase expliquant les clients de Zara
print("Les clients de Zara sont==>", brand["type_of_clothes"])
# #Ajout d'une clé appelée country_creation avec une valeur de Spain
brand["country_creation"] = "Spain"
 #Vérification de l'existance de la clé international_competitors dans le dictionnaire et si c'est le cas, ajout dans le magasin Desigua
if brand["international_competitors"] :
    brand["international_competitors"].append("Desigual")
# #suppression des informations sur la date de création
del brand["creation_date"]
 #Impression du dernier concurrent international.
print(brand["international_competitors"][-1])
#impression des principales couleurs de vêtements aux États-Unis.
print(brand["major_color"]["US"])
# #Impression du nombre de paires clé-valeur (c'est-à-dire la longueur du dictionnaire).
print(len(brand.keys()))
 #Impression des clés du dictionnaire.
print(brand.keys())
#. Création d'un autre dictionnaire appelé more_on_zaraavec les détails suivants :
more_on_zara = {
    "creation_date": 1975,
     "number_stores": 10000
 }
 # Utilisation d'une méthode pour ajouter les informations du dictionnaire more_on_zaraau dictionnaire brand

brand.update(more_on_zara)