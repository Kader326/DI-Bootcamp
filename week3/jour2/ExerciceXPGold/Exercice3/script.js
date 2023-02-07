//Créons un tableau vide. Par exemple : let shoppingList=[] .
let shoppingList=[]

//Créez un formulaire contenant : un champ de saisie de texte et un bouton « AddItem ». Ajoutez ce formulaire au DOM
newform=document.createElement("form");
newinput=document.createElement("input");
newinput.setAttribute("placeholder","your artile")
newinput.setAttribute("id","val");
newbutton=document.createElement("button");
newText= document.createTextNode("AddItem");
newbutton.setAttribute("onclick","addItem()");
newbutton.appendChild(newText);
newbutton.addEventListener("click",function(event){
event.preventDefault()
});
newform.appendChild(newinput);
newform.appendChild(newbutton);
document.getElementById("root").appendChild(newform);
//Tapez ce que vous devez acheter dans le champ de saisie de texte, puis ajoutez le nouvel article au tableau dès que vous cliquez sur le bouton "AddItem" ( Astuce : créez une fonction nommée addItem()).
function addItem(){
	var select=document.getElementById("val").value;
	console.log(select);
	shoppingList[shoppingList.length]=select;
	console.log("votre liste de courses")
	for (const element of shoppingList){
		console.log(element);
		alert(element)
	}

}	
//Ajoutez un bouton "ClearAll" au DOM, qui, une fois cliqué, devrait appeler la clearAll()fonction (voir ci-dessous).
newbutton2=document.createElement("button");
newText2 = document.createTextNode("clearAll");
newbutton2.setAttribute("onclick","clearAll()");
newbutton2.appendChild(newText2);
newbutton2.addEventListener("click",function(event){
event.preventDefault()
});

//Créez une fonction nommée clearAll()qui doit effacer tous les éléments de la liste de courses.
document.getElementById("root").appendChild(newbutton2);
		function clearAll(){
			console.log(shoppingList)
			shoppingList.length=0;
			console.log("votre liste de courses est vide");
			alert("votre liste de courses est vide");
		}