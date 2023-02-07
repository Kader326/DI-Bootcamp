let c;
let a=34;
let b=21;
console.log(a+b);
//1- prédiction: c'est la somme des deux nombres 34+25
//Actual:55

a=2;
console.log(a+b);
/* 2- prédiction:on vient de déclarer une nouvelle variable portant le meme nom, automatiquement il écrase
la valeur de la première valeur en prenant la deuxième valeur récente*/
//Actual:23


//3- La valeur de C est non définie donc undefined

console.log(3+4+'5');
//4- Le resultat donne 75