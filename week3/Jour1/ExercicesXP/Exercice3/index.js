//2- Dans le <div>,modifiez la valeur de l'attribut id de navBar à socialNetworkNavigation , à l'aide de la setAttributeméthode .
document.getElementById("navBar").setAttribute("id","socialNetworkNavigation");

//3-1 créons une nouvelle <li>balise (utilisez la createElementméthode).
let nouvelElement=document.createElement("li");

//3-2 Créons un nouveau nœud de texte avec "Déconnexion" comme texte spécifié.
let nouveauNoeud=document.createTextNode("Déconnexion");

//3-3 Ajoutons le nœud de texte au nœud de liste nouvellement créé ( <li>).
nouvelElement.appendChild(nouveauNoeud);

//3-4 Enfin,ajoutons ce nœud de liste mis à jour à la liste non ordonnée ( <ul>), en utilisant la appendChildméthode.
let noeudAjour=document.getElementById("socialNetworkNavigation").children[0];
noeudAjour.appendChild(nouvelElement);



