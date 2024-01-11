### Exercice 6: Personnel académique
# Créez une classe Personne avec des attributs tels que nom et age. Ensuite, créez 
# une classe Enseignant qui hérite de Personne et ajoute un attribut pour la matière enseignée. 
# Créez une autre classe Etudiant qui hérite également de Personne et ajoute un attribut pour le niveau d'études.

class Personne():
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

class Enseignant(Personne):
    def __init__(self, nom, age, matiere_enseignee):
        super().__init__(nom, age)
        self.matiere_enseignee = matiere_enseignee
    def info(self):
        print(f"{self.nom},{self.age} ans est enseignant de : {self.matiere_enseignee}.")

class Etudiant(Personne):
    def __init__(self, nom, age, niveau_detudes):
        super().__init__(nom, age)
        self.niveau_detudes = niveau_detudes
    def info(self):
        print(f"{self.nom}, {self.age} ans, a un niveau d'études de {self.niveau_detudes} ans.")

# Test Enseignant1
Enseignant1 = Enseignant("Mr.Henri",34,"Francais")
Info_Enseignant1 = Enseignant1.info()
Info_Enseignant1

# Test Etudiant1
Etudiant1 = Etudiant("Justin",24,5)
Info_Etudiant1 = Etudiant1.info()
Info_Etudiant1




