#Définition d'une classe appelée Song
class Song:
	def __init__(self,lyrics):
		self.lyrics=lyrics
#La methode sing_me_a_song et impression
	def sing_me_a_song(self):
		for i in self.lyrics:
			print(i)	
#création d'un objert , copie de l'objet exemple donné clairement				
toto_objet= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
toto_objet.sing_me_a_song()