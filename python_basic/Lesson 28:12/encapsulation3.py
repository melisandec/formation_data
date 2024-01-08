class Voiture:
    def __init__(self, marque, modele):
        self.__marque = marque
        self.__modele = modele

    @property
    def marque(self):
        return self.__marque

    @property
    def modele(self):
        return self.__modele

    @marque.setter
    def marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    @modele.setter
    def modele(self, nouveau_modele):
        self.__modele = nouveau_modele

# Utilisation de la classe
voiture1 = Voiture("Toyota", "Corolla")
print(voiture1.marque)  # Accès à l'attribut privé via la propriété
print(voiture1.modele)
voiture1.modele = "Camry"  # Modification du modèle via la propriété
print(voiture1.modele)