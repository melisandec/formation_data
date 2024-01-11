# Exercice 5: Véhicules
# Créez une classe de base appelée Vehicule avec des attributs tels que marque et annee. 
# Ensuite, créez des sous-classes pour différents types de véhicules (par exemple, Voiture, Moto) 
# avec des attributs spécifiques à chaque type.

class vehicule():
    def __init__(self,marque,annee):
        """Une classe de vehicule avec attributs marque année"""
        self.marque = marque
        self.annee = annee
    def lamarque(self):
        return self.marque
        
class voiture(vehicule):
    """Une sous-classe de vehicule qui reprends les attributs de 
    vehicule ainsi qu'un nouveau attribut : vitesse max"""
    def __init__(self,marque,annee,vitess_max_km):
        super().__init__(marque,annee)
        self.vitess_max_km = vitess_max_km
    def info(self):
        """Print une phrase avec tous les info sur la voiture"""
        print(f"Les {self.marque} de l'année {self.annee} ont une vitess maximum de {self.vitess_max_km} km/h.")

class moto(vehicule):
    """Une sous-classe de vehicule qui reprends les attributs de 
    vehicule ainsi qu'un nouveau attribut : prix"""
    def __init__(self, marque, annee,prix):
        super().__init__(marque, annee)
        self.prix = prix
    def info(self):
        """Print une phrase avec tous les info sur la voiture"""
        print(f"Une {self.marque} de l'année {self.annee} est disponible pour {self.prix}€.")

# Test marque - vehicule
vehicule1 = vehicule("BMW",2004)
Marque_vehicule1 = vehicule1.lamarque()
print(Marque_vehicule1)

# Test marque - voiture(vehicule)
voiture1 = voiture("BMW",2004,180)
Marque_voiture1 = voiture1.lamarque()
print(Marque_voiture1)

# Test info - voiture(vehicule)
voiture2 = voiture("Porche",2020,260)
Info_voiture2 = voiture1.info()
Info_voiture2

# Test info - moto(vehicule)
moto1 = moto("Vespa",2005,5600)
Info_moto1 = moto1.info()
Info_moto1