#Récupération du bout de code donné par l'exercice
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
#Accès à la clé salaire imbriquée à partir de la chaîne JSON ci-dessus
sampleJson = json.loads(sampleJson)
print(sampleJson['company']["employee"]['payable']['salary'])
#Ajout d'une clé appelée "birth_gate" à la chaine JSON au même niveau que la clé Name
sampleJson['company']['employee'].update({'birth_date':''})
print(sampleJson)

#Enregistrement du dictionnaire au format JSON dans un fichier
import json
jsonFile = 'fichier.json'
with open(jsonFile,'w') as jF:
    json.dump(sampleJson,jF)