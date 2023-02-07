wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 
def playTheGame():								
	print('list of words')
	print(wordslist)
	uword=input('choose a word :')
	while(uword not in wordslist):
		uword=input('word must be in the list so choose a word :')
	hiddenWord = "*"*len(word)
	print(hiddenWord)
	hidden = word.split("");
playTheGame()
