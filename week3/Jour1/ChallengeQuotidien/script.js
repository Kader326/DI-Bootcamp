//Créons un tableau dont la valeur est les planètes du système solaire.
var planetes=["Mars","Jupiter","Saturn","Mercury","Uranus","Neptune","Venus","Earth"];
console.log(planetes);
//Pour chaque planète du tableau, créons un <div>fichier using createElement. Cette div doit avoir une classe nommée "planet".
div_planete=[];
	new_planete=[];
	newTextNode=[];
	for (let i=0 ; i<8 ; i++) {
		div_planete[i]=document.createElement('div')
		new_planete[i]=document.createElement('p')
		newTextNode[i] = document.createTextNode(planets[i]);
		console.log(newTextNode[i]);
		new_planete[i].appendChild(newTextNode[i]);
		div_planete[i].appendChild(new_planete[i]);
		div_planete[i].setAttribute("class","planet");
		console.log(div_planete[i]);

//Chaque planète doit avoir une couleur de fond différente. ( Astuce : vous pouvez ajouter une nouvelle classe à chaque planète - chaque classe contenant une couleur de fond différente).
div_planete[i].classList.add("planet"+(i+1));
div_planete[i].style.backgroundColor="rgb(1"+(5*i)+"1,1"+(1*i)+"1,1"+(3*i)+"1)";
console.log(div_planete[i]);

//Enfin, ajout de chaque div au <section>dans le HTML (présenté ci-dessous).
var changement=document.body.lastElementChild.previousElementSibling;
console.log(changement);
changement.appendChild(div_planete[i]);
change1=document.getElementsByClassName("toto");
changet=document.getElementsByClassName("tata");
console.log(change1);
document.body.style.marging="auto"
for (const elements of change1) {
	elements.style.display="inline";
	}
for (const element of changet) {
	element.style.display="inline-block";
	}
}
    
//Defis terminé 