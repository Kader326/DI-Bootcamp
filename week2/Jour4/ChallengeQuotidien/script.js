let mots=prompt("Entrez des mots séparés par des virgules ")
mots=mots.split(",");
let etoileLongue=0;
let etoile="*";

for(let chaine of mots){
    if(etoileLongue<chaine.length){
        etoileLongue=chaine.length;
    }

    for (let i=0;i<chaine.length;i++){
        if(i==0){
            console.log("*".padStart((max+4),"*"));
        }
        console.log("* " +phrase[i].concat("".padStart(((max+4)-2)-(2+phrase[i].length)), " ") +"*");
        if(i==phrase.length-1){
            console.log("*".padStart((max+4),"*"));
        }
    }
}