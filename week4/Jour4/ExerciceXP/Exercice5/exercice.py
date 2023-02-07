#Écrivons une fonction appelée make_shirt()qui accepte une taille et le texte d'un message qui doit être imprimé sur la chemise.
def make_shirt(taille=45,texte_of_message="I love python"):
    print(f"La taille de la chemise est {taille} et le texte est==>{texte_of_message}")
make_shirt(32, "M. Malick est super instructeur")
#Réalisation d'une grande chemise avec le message par défaut
make_shirt(100)
#Réalisation d'une moyenne chemise avec le message par défaut
make_shirt(55)
#Réalisation d'une chemise de taille quelconque avec un message différent
make_shirt(48, "M. Malick est super cool")

