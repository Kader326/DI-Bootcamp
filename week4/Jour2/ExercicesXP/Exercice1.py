from ntpath import join


my_fav_numbers={18,19,20,15,17}

my_fav_numbers.update([14,16]) #Ajout de deux nouveaux numéros à l'ensemble
print(my_fav_numbers)

my_fav_numbers.remove(20) #Supprime le dernier numéro du set
print(my_fav_numbers)

friend_fav_numbers={21,54,96,78,12}
our_fav_numbers=my_fav_numbers | friend_fav_numbers #Concaténation de deux sets.
print(our_fav_numbers)