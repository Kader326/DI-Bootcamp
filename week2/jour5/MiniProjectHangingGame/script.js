function verifTaille(mot) {
    if (mot.length < 8)
        return false;
    else
        return true;
}

function entrezMot(){
    let mot;
    do{
        mot = prompt("Entrez un mot de 8 lettres minimum"); 
    } while (!verifTaille(mot))
    return mot;
}


//2
function verifLettre(lettre) {
    if (lettre.length != 1)
        return false;
    else
        return true;
}

function entrezLettre() {
    let lettre;
    do {
        lettre = prompt("Entrez une lettre");
    } while(!verifLettre(lettre))
    return lettre;
}

function verif(mot,mot1,lettre) {
    let mot2 = "";
    for(let i = 0; i < mot.length; i++){
        if ( mot[i] == lettre && lettre != mot1[i]) {
            mot2 += mot[i];
        } else {
            mot2 += mot1[i];
        }
    }
    return mot2;
}

function timeOut(mot1,mot2) {
    if (mot1 == mot2)
        return false;
    else {
        return true;
    }
}



function jeuPendu() {
    let mot = entrezMot();
    let mot1 = "*".repeat(mot.length);
    console.log(mot1);
    let error = 0;
    do {
        let lettre = entrezLettre();
        let mot2 = verif(mot,mot1,lettre);
        if (timeOut(mot1,mot2)){
            mot1 = mot2;
            console.log(mot1);;
        } else {
            error += 1;
            console.log("Try again");
        }
        
        if (mot1 == mot) {
            console.log("CONGRATS YOU WIN")
            return;
        }
        if (error == 10)
            console.log("YOU LOSE");
    } while( error < 10)
}

jeuPendu();