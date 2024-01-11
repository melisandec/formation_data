### Exercice 2: Employés et Managers
# Créez une classe Employe avec des attributs tels que nom et salaire. Ensuite, créez une sous-classe Manager 
# qui hérite de Employe et ajoute un attribut supplémentaire pour le nombre d'employés sous sa supervision. 
# Surchargez la méthode de calcul du salaire pour inclure une prime basée sur le nombre d'employés supervisés.

class Employes:
    def __init__(self,nom,salaire):
        """Créez une classe Employe avec des attributs tels que nom et salaire."""
        self.nom = nom
        self.salaire = salaire
    def calculer_salaire(self):
        return self.salaire

class Manager(Employes):
    def __init__(self,nom, salaire,n_employés_sous_supervision):
        """créez une sous-classe Manager qui hérite de Employe et ajoute un attribut 
        supplémentaire pour le nombre d'employés sous sa supervision."""
        self.n_employés_sous_supervision = n_employés_sous_supervision

    def calculer_salaire(self):
        return self.salaire + (400*self.n_employés_sous_supervision)


Employe1 = Employes("Joe",45000)
salaire_Employe1 = Employe1.calculer_salaire()
print(salaire_Employe1)

Manager1 = Manager("Joe",45000,5)
salaire_Manager = Manager1.calculer_salaire()
print(salaire_Manager)

    