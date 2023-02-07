//Affichage de la valeur de l'option sélectionnée.
console.log(document.querySelectorAll('[selected]'));
var select1=document.querySelectorAll('[selected]')[0].value
console.log(select1)
alert(select1)
//Ajout d'une option supplémentaire au selecttag :
newoption=document.createElement("option");
newoption.setAttribute("value","classic");
newText= document.createTextNode("classic");
newoption.appendChild(newText);
console.log(newoption);
document.getElementById("genres").appendChild(newoption)


//L'option nouvellement ajoutée doit être sélectionnée par défaut.
document.getElementById("genres").children[2].selected=true;
console.log(document.getElementById("genres").children[2]);
