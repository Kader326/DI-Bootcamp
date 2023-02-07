//2-Couleur d'arrière plan et un padding au div.
document.getElementsByTagName("div")[0].style.backgroundColor="Blue";
document.getElementsByTagName("div")[0].style.padding="15px";

//3- Ne pas afficher le <li> qui contient le noeud texte john.
let nonAfficheJohn=document.getElementsByTagName("li");
document.getElementsByTagName("ul")[0].removeChild(nonAfficheJohn[0]);

//4-Ajoutons une bordure au <li> qui contient le nœud de texte "Pete".
document.getElementsByTagName("li")[0].style.border="3px solid green";

//5-Modifiez la taille de la police de tout le corps.
document.getElementsByTagName("body")[0].style.fontSize="50px";


