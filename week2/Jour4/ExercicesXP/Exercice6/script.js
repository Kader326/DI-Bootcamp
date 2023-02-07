function hotelCost(){
        let nombreNuit=Number(prompt("Combien de nuits souhaitez-vous séjourner :"));//Demande le nombre de nuits que l'utilisateur veut passer dans l'hotel.
        let prixTotalHotel=nombreNuit*140; //Calcul le prix total de l'hotel.
        console.log(prixTotalHotel); // Affiche le prix total de l'hotel.
    }
    hotelCost()


function planeRideCost(){
    let destination=prompt("Quelle est votre destination: "); //Demande à l'utilisateur la destination ou il veut s'y rendre.
    if(destination=="Londres"){ // si destination est londres affiche le prix.
        console.log(183+"$");
    }
    else if(destination=="Paris"){ // ou si destination est Paris affiche le prix.
        console.log(220+"$");
    }

    else{
        console.log(300+"$"); // sinon autre destination que paris, affiche le prix également.
    }
}
planeRideCost()


function rentalCarCost(){
    let nombreJours=Number(prompt("Combien de jours souhaitez-vous louer la voiture :")); //Demande à l'utilisateur combien de jours pour la location de la voiture.
    CoutLocationVoiture=nombreJours*40 // calcul la location de la voiture.
    if(nombreJours>10){ // si location de voiture est supérieur à 10 faire une réduction de 5%.
        let reduction=CoutLocationVoiture*0.05; // calcul de la réduction de la voiture.
        let redutionTotal=CoutLocationVoiture-reduction;
        console.log("Le prix total de la location de voiture est: " +redutionTotal); //Affiche la réduction.
    }
    else{
        console.log("Le prix total de la location de voiture est: "+CoutLocationVoiture)// Affiche coutLocationVoiture.
    }
}
rentalCarCost()


function totalVacationCost(){ // Appel des différentes fonctions.
   hotelCost()
   planeRideCost()
   rentalCarCost()
}
totalVacationCost()