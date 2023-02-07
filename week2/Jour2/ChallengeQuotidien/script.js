//let sentence="the teacher must not change his lesson which is so bad";
let sentence=prompt("Entrez une chaine contenant les mots bad et not :")
sentence=sentence.split(" ");
let wordNot=sentence.indexOf("not");
let wordBad=sentence.indexOf("bad");

if(wordBad){
    wordBad=sentence.indexOf("bad");
}

if(wordBad>wordNot&& wordBad!=-1 && wordNot!=-1){
    sentence.splice(wordNot,wordNot+1,"good");
    sentence.join(" ");
}

else if(wordBad){
    wordBad=sentence.indexOf("bad");
    sentence.splice(wordNot,wordBad+1,"good");
    sentence=sentence.join(" ");
}

else{
    sentence=sentence.join(" ");
}
console.log(sentence);




