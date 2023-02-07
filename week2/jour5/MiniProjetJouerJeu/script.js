//Première Partie
function playTheGame(){
    if (confirm("Souhaitez vous jouer au jeu ?==>") == false) 
    {
         alert("Pas de problème. Au revoir");
    } 
    else 
    {
       let numero = prompt("Svp, entrer un numero compris entre 1 et 10==>");
       numero = Number(numero);
       if (!numero)
       {
       	console.log("Désolé! C'est pas un numéro, au revoir");
       }
       else if (numero < 0 && numero > 10)
       {
       	console.log("Désolé! Ce n'est pas un bon chiffre, au revoir");
       }
       else 
       {
		min = Math.ceil(min);
		max = Math.floor(max+1);
		let computerNumber = Math.floor(Math.random()* (max - min)) + min;
		console.log(computerNumber);       
		}
	}
}

//deuxième partie
		function compareNumbers(userNumber,computerNumber) {
		let i=0;
		while(i<3) {
			if (userNumber == computerNumber) {
				alert("WINNER");
				return true;
			} else if (userNumber > computerNumber) {
				userNumber = prompt("Votre numéro est supérieur à celui de l'ordinateur, donner un autre"); 
			}
			else if (userNumber < computerNumber) {
				userNumber = prompt("Votre numéro est inférieur à celui de l'ordinateur, donner un autre"); 
			}	
			else if ( i == 3) {
				alert("Vous n'avez pas de chances");
				return;
			}
			i++;
		}
	}