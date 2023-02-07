#Nombre parfait
nombre = int(input("Entrez un nombre : "))
parfait = 0
for i in range(1,nombre) :
    if nombre%i == 0 :
        parfait += i
if parfait == nombre :
    print(nombre,"est un nombre parfait")
else :
    print(nombre,"n'est pas un nombre parfait")