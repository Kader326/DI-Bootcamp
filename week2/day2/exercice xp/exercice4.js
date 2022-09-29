let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
users.length
 if ( users.length=== 0) {
        console.log("personne n'est en ligne")
    } else if ( users.length=== 1) {
        console.log("est en ligne":users[0])
    } else if ( users.length=== 2) {
        console.log("est en ligne":users[0],users[1])
    }
    else ( users.length>2){
        newusers=users.length-2
        console.log("les deux premiers noms dans le tableau des utilisateurs sont":users[0],users[1]"et le nombre d'utilisateur supplémentaire sont" :newusers)
    }