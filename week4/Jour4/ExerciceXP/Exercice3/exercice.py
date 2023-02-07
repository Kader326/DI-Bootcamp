#Écriture d'une fonction appelée describe_city()qui accepte le nom d'une ville et son pays comme paramètres.
def describe_city(ville_name,country_name="Israèl"):
    print(f"{ville_name} is in {country_name}")
describe_city("Ouagadougou","Burkina faso")
#test du paramétrage du pays par défaut
describe_city("Ouagadougou")