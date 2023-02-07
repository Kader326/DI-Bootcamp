//Ajoutez de nombreux écouteurs d'événements à un élément de votre page Web. Utilisez les événements click, mouseoveret .mouseoutdblclick
//Chaque auditeur doit faire une chose différente, par exemple - changer la position x, changer la position y, changer la couleur, changer la taille de la police… et plus encore
document.body.children[0].addEventListener("click",function(){
    Default()
});
function Default(){
document.body.children[0].style.fontSize="12px";
document.body.children[0].style.backgroundColor="black";
document.body.style.backgroundColor="gray";
document.body.children[0].style.color="white"
}
document.body.children[0].setAttribute('ondblclick','change1()')
document.body.children[0].setAttribute("mouseover","nochange()")
document.body.children[0].setAttribute("mouseout","change2()")

function change1(){
    document.body.children[0].style.fontSize="100px";
    document.body.children[0].style.backgroundColor="red";
    document.body.style.backgroundColor="orange";
    document.body.children[0].style.color="white"
}
function change2(){
    document.body.children[0].style.border="solid black 3px";
    document.body.children[0].style.backgroundColor="blue";
    document.body.style.backgroundColor="yellow";
    document.body.children[0].style.color="white"
}
function nochange(){
    document.body.children[0].style.fontSize="70px";
    document.body.children[0].style.backgroundColor="red";
    document.body.style.backgroundColor="orange";
    document.body.children[0].style.color="white"
}








