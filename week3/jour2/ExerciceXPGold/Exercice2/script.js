//Ajoutez un clickécouteur d'événement au <input type="button">. Lorsque vous cliquez dessus, il doit appeler une fonction nommée : removecolor()qui supprime la couleur sélectionnée de la liste déroulante
console.log(document.getElementById("colorSelect").nextElementSibling);
var select1=document.getElementById("colorSelect").nextElementSibling;
select1.setAttribute("onclick","removecolor()")
function removecolor(){
	select2=document.getElementById("colorSelect").value;
	console.log(select2);
	var Aray=document.getElementsByTagName("option");
	for (const elements of Aray ) {
		if(elements.textContent===select2){
			elements.outerHTML="";	
		}
		
	}
}