# Exercise 1
# Créer une classe qui va s'appeler forme et sortir formule de l'aire et du perimetre. Commencer avec rectangle.

class Forme():
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur

    def get_aire() :
        aire = longueur*largeur
        return(aire)
    
    def get_perimetre():
        perimetre = longueur*2 + largeur*2
        return(perimetre)


rectange = Forme(40,30)
print(rectange.get_aire)
