let people=["Greg","Mary","Devon","James"]
people.shift()  //Supprime Greg du tableau
console.log(people)

people[2]="jason"    // remplace james par jason
console.log(people)

people.push("Patrick") //ajoute mon nom à la fin du tableau
console.log(people)

console.log(people.indexOf("Mary")) //Affiche l'index de Mary

console.log(people.slice(1,3)) //copie du people tableau

console.log(people.indexOf("Foo")) //Index de fofo

let last=people.pop()  //renvoie le dernier élément du tableau
console.log(last)

for(let AfficherPeople of people){ //Parcourir le tableau et afficher chaque personne
    console.log(""+AfficherPeople)

}

for (let AfficherPeople of people){
     if(people=="jason") {
      console.log(AfficherPeople)
        break;
     }
    }