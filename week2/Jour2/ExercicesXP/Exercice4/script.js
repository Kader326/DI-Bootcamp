let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
console.log(users.length);
if(users==0){
    console.log("personne n'est en ligne");
}

else if(users.length==1){
    console.log(users);
}

else if(users.length==2){
    console.log(users);
}

else{
    console.log(users[0],",",users[1],",","Aurelia",",","Roland",",","Eddie");
}
