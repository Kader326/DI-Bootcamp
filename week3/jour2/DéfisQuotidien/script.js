//Obtention la valeur de chacune des entrées dans le fichier HTML lorsque le formulaire est soumis. Se souvenir duevent.preventDefault()
var select1=document.body.children[1].children[15];
console.log(select1);
select1.addEventListener("click",function(event){
event.preventDefault()
});
var changeNoun;
var changeAdj;
var changeName;
var changeVerb;
var changePlace;
select1.setAttribute("onclick","calc()")
function calc(){
	changeNoun=document.getElementById("noun").value;
	console.log("noun="+changeNoun);
	changeAdj=document.getElementById("adjective").value;
	console.log("adjective= "+changeAdj);
	changeName=document.getElementById("person").value;
	console.log("person= "+changeName);
	changeVerb=document.getElementById("verb").value;
	console.log("verb="+changeVerb);
	changePlace=document.getElementById("place").value;
	console.log("place= "+changePlace);

//Les valurs ne sont pas vides
			if(changeNoun!=='' && changeAdj!=='' && changeName!=='' && changeVerb!=='' && changePlace!==''){
				console.log("valid inputs story will be display");
				alert("valid inputs story will be display");
				newp=document.createElement("p");
				newbutton=document.createElement("button");
				newbutton.setAttribute("onclick","news()");
				newTexts= document.createTextNode("click here to change the story");

//Les histoires à raconter
				newText= document.createTextNode("\" "+changeNoun+" vous êtes un hommeou une femme mais......une chose est sure"+changeVerb+" il ou elle, c'est drôle. L' "+changeAdj+" peut attendre une qualification "+changePlace+" et pourquoi il ou elle en tant que voilàààà quoi "+changeName+" \"");
				newp.appendChild(newText);
				console.log(newText);
				console.log(newp);
				document.getElementById("story").appendChild(newText);
			}else{
				console.log("Vous avez des entrées valides");
				alert("Vos entrées ne sont pas valides");
			}

		}