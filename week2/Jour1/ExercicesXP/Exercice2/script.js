let myWatchedSeries=["black mirror", "money heist","the big bang theory"];

let myWatchedSeriesLength=myWatchedSeries.length; // nombre de séries dans myWatchedSeries

console.log(myWatchedSeriesLength); //Affichage du nombre de déries

let myWatchedSeriesSentence="prison break, Scorpion,Raymond Raddington"; // phrase décrivant la série dont vous regardez

console.log(myWatchedSeriesSentence); //Affichage de la phrase décrivant la série

console.log("je regarde trois séries préférées qui sont: "+myWatchedSeriesSentence); //phrase montrant les deux variables créees ci-dessus

myWatchedSeries[2]="friends"; //Remplacement de la série big bang theory par friends

console.log(myWatchedSeries); // Affichage du remplacement série big bang theory par friends

myWatchedSeries.push("Casa papel"); // Ajout à la fin du tableau le nom d'une série

console.log(myWatchedSeries); //Affichage de la série ajoutée

myWatchedSeries.unshift("24heures Chrono"); //Ajout au debut du tableau une série

console.log(myWatchedSeries); //Affichage de l'ajout d'une série au debut 

myWatchedSeries.splice(1,1); // suppression d'une série dans le tableau à partir de sa position et le nombre d'éléments à supprimer

console.log(myWatchedSeries); //Affichage de la suppression d'une série dans le tableau

console.log("money heist".indexOf("mon",3)); //Affichage de la troisième lettre de la série money heist

console.log(myWatchedSeries); //Affichage pour voir toutes les modifications apportées