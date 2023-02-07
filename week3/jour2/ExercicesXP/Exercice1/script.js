//Exercice 1 : Modification d'articles
//Récupération de h1 et console.log
console.log(document.body.firstElementChild.firstElementChild.textContent);
//Suppression du dernier paragraphe
document.body.firstElementChild.lastElementChild.outerHTML=" ";
console.log(document.body.firstElementChild.lastElementChild);
//Ajout d'un écouteur d'évènement qui changera la couleur d'arrière plan du h2 en rouge
console.log(document.body.firstElementChild.firstElementChild.nextElementSibling);
document.body.firstElementChild.firstElementChild.nextElementSibling.setAttribute("onclick","color()");	
function color(){
	document.body.firstElementChild.firstElementChild.nextElementSibling.style.backgroundColor="red"
	}
//Ajout d'un écouteur d'évènement qui masquera le h3 lorsqu'il est cliqué
console.log(document.body.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling);
document.body.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling.setAttribute("onclick","hider()");
function hider(){
	document.body.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling.style.display="none"
		}
//Ajout d'un bouton au fichier html qui lorsqu'on clique dessus met tous les paragraphes en gras
newbutton=document.createElement("button");
console.log(newbutton);
newbutton.textContent='cliquez ici pour mettre les paragraphes en gras'
newbutton.setAttribute("onclick","bolder()");
function bolder(){
	document.body.style.fontWeight="bold"
	}
document.body.appendChild(newbutton);


