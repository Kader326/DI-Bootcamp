function bouteilles() {
    let number_of_bottles = prompt("Svp, donner un nombre de bouteille");
    number_of_bottles = Number(number_of_bottles);
    console.log("We start the song at " + number_of_bottles + " bottles");

    number_of_bottles= number_of_bottles-1;
    console.log("Take _1_ down, pass it around");
    console.log("we have now " + number_of_bottles + " bottles");
    for ( let i = 1; i < number_of_bottles; i++) 
    {
        console.log("Take _" + i + "_ down, pass them around");
        number_of_bottles = number_of_bottles-i;
        console.log("we have now " + number_of_bottles + " bottles");
    }
    console.log("Take _" + number_of_bottles + "_ down, pass them around");
    console.log("-> we have now 0 bottle");
}

bouteilles()