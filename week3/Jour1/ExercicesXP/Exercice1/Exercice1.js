//1-Récupérer le div et l'afficher
console.log(document.getElementById("container").innerHTML);

//2-Changer le nom pete en richard
let richard= document.getElementsByTagName("li");
for(let i=0;i<richard.length;i++){
    if(richard[i].innerHTML=="Pete"){
      richard[i].innerHTML="Richard";
    }
}


//3-Remplacer chaque prénom des deux <ul> par votre nom
let chaquePrenom=document.getElementsByTagName("li");
for(let i =0; i<chaquePrenom.length;i++){
    chaquePrenom[i].innerHTML="ZAGRE";
}


//4-Supprimrer le noeud de texte qui contient sarah
let remplacerSarah=document.getElementsByTagName("ul");
for(let i=0;i<remplacerSarah.length;i++){
    if(remplacerSarah[i].innerHTML=="Sarah"){
     remplacerSarah[1].removeChild(richard[i]);
      }
}