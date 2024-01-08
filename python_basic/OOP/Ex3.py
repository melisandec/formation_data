### Exercice 3: Animaux
# Créez une classe de base appelée Animal avec des attributs tels que nom et age. 
#Créez ensuite des sous-classes pour différents types d'animaux (par exemple, Chien, Chat) 
# avec des caractéristiques spécifiques à chaque type.

class Animaux():
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age

class chien(Animaux):
    def promenade(self):
        print("A besoin de 3 promenade par jour")

class chat(Animaux):
    def mange(self):
        print("Mange 2 fois par jours")

Animal1 = Animaux("bob",2)

Chien1 = chien("bob",2)
Chien1.promenade()
Chat1 = chat("Momo",6)
Chat1.mange()