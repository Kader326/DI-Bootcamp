function isDivisible(){
    let somme=0;
    for(let i=0;i<500;i++){ //Parcourir les nombres de 0 à 500.
          if (i%23==0){ 
            console.log(i);
            somme+=i;  //fait la somme de l'intervalle du nombre de 0 à 500.
    }
    }
    console.log("La somme de tous les nombres est :"+somme) //Affiche la somme du diviseur 23.
}
isDivisible()


//Bonus
function isDivisible(divisor){
    let somme=0;
    for(let i=0;i<500;i++){ // Parcourir les nombres de 0 à 500.
          if (i%divisor==0){
            console.log(i);
            somme+=i; //fait la somme du nombre de l'intervalle de 0 à 500.
    }
    }
    console.log("La somme de tous les nombres est :"+somme) //Affiche la somme du diviseur du nombre saisi par l'utilisateur.
}
isDivisible(Number(prompt("Entrez le diviseur : ")))//L'utilisateur saisit le diviseur.



