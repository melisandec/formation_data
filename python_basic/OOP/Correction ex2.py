class Employe:
    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire

    def calculer_salaire(self):
        return self.salaire

class Manager(Employe):
    def __init__(self, nom, salaire, nb_employes):
        super().__init__(nom, salaire)
        self.nb_employes = nb_employes

    def calculer_salaire(self):
        return super().calculer_salaire() + self.nb_employes * 1000



# Création d'un employé
employe1 = Employe("Alice", 50000)
salaire_employe