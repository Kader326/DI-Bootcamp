	let sentence =prompt( "Entrez une phrase contenant le mot not et bad", "The movie is not that bad, I like it");
	sentence = sentence.split(" ");
//2
	let wordNot = sentence.indexOf("not");
//3
	let wordBad = sentence.indexOf("bad");
	if (wordBad) {
		wordBad = sentence.indexOf("bad,");
	}
//4
	if (wordBad > wordNot && wordBad != -1 && wordNot != -1) {
		sentence.splice(wordNot,wordBad-wordNot+1,"good");
		sentence = sentence.join(" ");
	} else if (wordBad) {
		wordBad = sentence.indexOf("bad,");
		sentence.splice(wordNot,wordBad-wordNot+1,"good,");
		sentence = sentence.join(" ");	
	}
//5
	else {
		sentence = sentence.join(" ");
	}
	console.log(sentence);