#Création d'un programme qui imprime une liste des articles que vous pouvez acheter dans le magasin avec l'argent que vous avez dans votre portefeuille.
items_purchase = {
   "Apple": "$4",
   "Honey": "$3",
   "Fan": "$14",
   "Bananas": "$4",
   "Pan": "$100",
   "Spoon": "$2"
 }

wallet = "$100" 
# #trie de la liste par ordre alphabétique
trie= items_purchase
print(trie)
achat =[]
for i in trie:
    if(int(trie[i][1:]) <= int(wallet[1:])):
          achat.append(i)
if achat == []:
    print("Nothing")
else : 
    print(achat)
#Défis terminé
def higest_even(li):
    evens = []
    for item in li:
         if item % 2 == 0:
              evens.append(item)
         return max(evens)
print(higest_even([4,5,7,9,9,9,9,9,9,9,9]))
def super_func(*args, **kwargs):
   total = 0
   for items in kwargs.values():
    total += items
    return sum(args) + total
print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))