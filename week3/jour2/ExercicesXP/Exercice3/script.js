
//Déclaration d'une variable globale
var allBoldItems=[]
//Créez une fonction appelée getBold_items()qui ne prend aucun paramètre. Cette fonction doit collecter tous les éléments en gras à l'intérieur du paragraphe et les affecter à la allBoldItemsvariable.
		function getBold_items(){
			var select=document.getElementsByTagName("strong");
			console.log(select);
			i=-1;
			for (const element of select) {
				i=i+1;
				allBoldItems[i]=element;
			}
			console.log(allBoldItems);
		}
		getBold_items()
//Créez une fonction appelée highlight()qui change la couleur de tout le texte en gras en bleu
		function highlight(){
			for (const elements of allBoldItems) {
			 	 elements.style.color="blue";
			}
		}
//Créez une fonction appelée return_normal()qui change la couleur de tout le texte en gras en noir.
		function return_normal(){
			for (const elements of allBoldItems) {
			 	 elements.style.color="black";
			}
		}
//Appelez la fonction highlight()sur mouseover (c'est-à-dire lorsque le pointeur de la souris est déplacé sur le paragraphe) et la fonction return_normal()sur mouseout (c'est-à-dire lorsque le pointeur de la souris est déplacé hors du paragraphe).
		var changer=document.body.children[0]
		changer.setAttribute("onmouseover","highlight()");
		changer.setAttribute("onmouseout","return_normal()");
		console.log(changer);
