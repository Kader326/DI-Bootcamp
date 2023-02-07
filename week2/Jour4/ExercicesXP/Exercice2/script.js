function calculateTip(){
    var facture=Number(prompt("Quel est le montant de la facture : ")) //saisir le montant de la facture.
    if(facture<50){   // si le montant de la facture est inférieur à 50 laissez un pourboire de 20%.
         var pourboire=facture*0.2;
    }

    else if((facture==50) && (facture==200)){ // sinon si le montant de la facture est comprise entre 50 et 200 laissez un pourboire de 15%.
        var pourboire=facture*0.15;
    }

    else{                //Sinon laissez un pourboire de 10%.
        var pourboire=facture*0.1;
    }

    console.log("Le montant du pourboire et de la facture sont: "+(facture+pourboire)) //Affiche du montant de la facture et du pourboire.
  }
  calculateTip() //Appel de la fonction.
