class CompteBancaire :
    def __init__(self,solde):
        self.__solde = solde # attribut privé

    def get_solde(self):
        return self.__solde
    
    def deposer(self,montant):
        self.__solde += montant

    def retirer(self,montant):
        if montant<=self.__solde:
            self.__solde -=montant
        else:
            print("Solde insuffisant")


# Exemple d'utilisation

compte = CompteBancaire(1000)
print("Solde initial : ",compte.get_solde())
compte.deposer(500)
print("Nouveau solde : ",compte.get_solde())
compte.retirer(200)
print("Nouveau solde apres retrait: ",compte.get_solde())
compte.retirer(2200)


