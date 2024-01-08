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

class Chat(Animal):
    def faire_son(self):
        print("MIAOU")

#Exemple d'utilisation
        
nom_chat = Chat("Mittens","chat")
nom_chat.afficher_info()
nom_chat.faire_son()

class Chien(Animal):
      def faire_son(self):
        print("OUF OUF")

      def son_repas(self):
          print("mange du poulet")



nom_chien = Chien("BIOB","chien")
nom_chien.afficher_info()
nom_chien.faire_son()
nom_chien.son_repas()