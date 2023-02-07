while(true){ 
    let numero=Number(prompt("Entrez un numero :"));// L'utilisateur entre un nombre, on convertit ce nombre en entier 
        if(numero<10){ //Condition si le nombre entré par l'utilisateur est inférieur à 10, si oui demandez de nouveau,sinon il sort de la boucle
        console.log("Entrer un nouveau numéro")
    }
    else{
        break;
    }

}

