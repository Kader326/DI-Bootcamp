keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionnary = dict(zip(keys,values))
print(dictionnary)

#exo2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
facture = 0;
for name, age in family.items():
    if 0<=age<3 :
        print(name, "ne paie rien.")
        
    elif 3<=age<=10 :
        print(name, "paie 10$")
        facture += 10
    elif age>10:
        print(name, "paie 15$" )
        facture += 15

print("La famille paie au total: ",facture)
#exo3
brand = {"name": "Zara", 
"creation_date": 1975, 
"creator_name": "Amancio Ortega Gaona",
"type_of_clothes":[ "men", "women", "children", "home"], 
"international_competitors": ["Gap", "H&M", "Benetton"], 
"number_stores": 7000, 
"major_color":{ 
    "France": "blue", 
    "Spain": "red", 
    "US": ["pink", "green"]}}

brand.update({"number_stores": 2})
brand["number_stores"]= 2

print(brand["type_of_clothes"])

brand["country_creation"]="Spain"

if brand["international_competitors"]:
    brand["international_competitors"].append("Desigual")

del(brand["creation_date"])

print((brand["international_competitors"])[-1])

print((brand["major_color"])["US"])

print(len(brand))

print(brand.keys())

more_on_zara = {"creation_date": 1975, 
"number_stores": 10000}

brand.update(more_on_zara)

print(brand["number_stores"])

#exo4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_user_A={users[i]: i for i in range(len(users))}
print(disney_user_A)

disney_user_B={i : users[i] for i in range(len(users))}
print(disney_user_B)

disney_user_C={users[i]: i for i in range(len(sorted(users, reverse ="false")))}
print(disney_user_C)

disney_user_D={users[i]: i for i in range(len(users)) if i in users}
print(disney_user_D)

disney_user_D={users[i]: i for i in range(len(users)) if i in users}
print(disney_user_D)

disney_user_E={users[i]: i for i in range(len(users)) if i in users[0]=="m" or users[0]=="p"}
print(disney_user_E)