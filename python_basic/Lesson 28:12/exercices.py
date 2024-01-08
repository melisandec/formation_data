import math 

class Forme:
    def air(self):
        pass


class Rectangle(Forme):
    def __init__(self,longeur,largeur):
        self.longueur = longeur
        self.largeur = largeur

    def air(self):
        return self.longueur * self.largeur
    

class Cercle(Forme):
    def __init__(self,rayon):
        self.rayon = rayon

    def air(self):
        return math.pi * self.rayon * self.rayon


#Exemple d'utilisation
rectangle = Rectangle(5,3)
print("Aire du rectangle : ",rectangle.air())

cercle = Cercle(4)
print("Aire du cercle -> ",cercle.air())