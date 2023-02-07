function changeEnough(itemPrice, amountOfChange){
        let quarters=amountOfChange[0]*0.25 ; //la valeur 1 de l'index 0 multiplier par 0.25.
        let dimes=amountOfChange[1]*0.1  ; //la valeur 2 de l'index 1 multiplier par 0.1.
        let nickel=amountOfChange[2]*0.05; //la valeur 3 de l'index 2 multiplier par 0.05.
        let penny=amountOfChange[3]*0.01 ; //la valeur 4 de l'index 3 multiplier par 0.01.
        let sommeChangement=quarters+dimes+nickel+penny ; //Fait la somme totale des différentes valeurs.
        if(sommeChangement>=itemPrice){  // si la somme totale est supérieure au prix de l'article return true.
            console.log("true")
        }
    
        else{
            console.log("false") // sinon return false.
        }
    }
changeEnough(4.25, [25, 20, 5, 0])
changeEnough(14.11, [2,100,0,0])
changeEnough(0.75, [0,0,20,5])
 
  

           
  