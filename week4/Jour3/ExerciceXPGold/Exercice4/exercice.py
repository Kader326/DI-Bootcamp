item = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
for cle,valeur in item.items():
    print(cle,"prix-->",valeur)
somme=0
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
    }
for cle,valeur in items.items():
    somme+=items[cle]['price']*items[cle]['stock']
print("Prix total:",somme)