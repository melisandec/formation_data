class Animal :
    def __init__(self,nom,espece):
        self.nom = nom
        self.espece = espece

    def faire_son(self):
        pass
    
    def afficher_info(self):
        """ decrire l'ojet de la fonction"""
        print(f"{self.nom} est un {self.espece}")

    
#Exemple d'utilisation

chat = Animal("BOB","chat")
chat.afficher_info()