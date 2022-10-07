/copie du tableau donné
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
//recherche du nom de la société
let nom_société = [];
//Récupération des lettres
for( let i in names){
	nom_société[i] = names[i][0];
	}
//trie par ordre alphabétique
nom_société = nom_société.sort();
//Jointure des éléments du tableau
nom_société = nom_société.join("");
console.log(nom_société);
//Affichage du nom de la société
console.log(nom_société);
