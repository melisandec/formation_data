class Personne:
    def __init__(self, nom, age):
        self.__nom = nom  # Attribut privé
        self.__age = age  # Attribut privé

    # Méthodes d'accès (getters)
    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    # Méthodes de modification (setters)
    def set_nom(self, nouveau_nom):
        self.__nom = nouveau_nom

    def set_age(self, nouvel_age):
        if nouvel_age > 0:
            self.__age = nouvel_age


personne1 = Personne("Alice",25)
print(personne1.get_nom())
print(personne1.get_age())

personne1.set_nom("Alicand")
print(personne1.get_nom())
personne1.set_age(26)  # Modification de l'âge via le setter
print(personne1.get_age())

