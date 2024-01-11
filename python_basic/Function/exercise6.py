## 1
# Générer le nombre secret : Créez une fonction generer_nombre_secret qui utilise le module random 
# pour générer un nombre aléatoire entre 1 et 100. Cette fonction sera appelée au début du jeu.

def generer_nombre_secret():
    from random import randint
    num = randint(1, 100) 
    return(num)

## 2
# Fonction de devinette : Créez une fonction deviner_nombre qui prend deux arguments, 
# le nombre secret et la tentative de l'utilisateur. 
# Cette fonction devrait renvoyer des indications telles que "Bravo !", "Le nombre est plus grand" ou "Le nombre est plus petit".

def deviner_nombre(generer_nombre_secret,tentative):
    if generer_nombre_secret == tentative:
        print("Bravo !")
    elif generer_nombre_secret > tentative:
        print("Le nombre est plus grand")
    else:
        print("Le nombre est plus petit")

## 3
# Boucle de jeu : Créez une fonction principale jeu_de_devinette qui appelle les fonctions précédentes. 
# Utilisez une boucle pour permettre à l'utilisateur de faire plusieurs tentatives.

def jeu_de_devinette(generer_nombre_secret,deviner_nombre):
    print("Bienvenue au jen de devinette")
    nombre_secret = generer_nombre_secret()
    essaie_max = 5
    for essaie in range(essaie_max):
        tentative = int(input("Deviner un nombre entre 1 et 100: "))
        resultat = deviner_nombre(nombre_secret,tentative)
        print(resultat)
        if tentative == nombre_secret:
            print(f"Nombre d'essais : {essaie + 1}")
            break
        else : 
            print(f"Dommage ! Le nombre secret était {nombre_secret}")



