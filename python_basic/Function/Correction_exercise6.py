import random

def generer_nombre_secret():
    return random.randint(1, 100)

def deviner_nombre(secret, tentative):
    if tentative == secret:
        return "Bravo ! Vous avez trouvé le nombre secret."
    elif tentative < secret:
        return "Le nombre est plus grand. Essayez à nouveau."
    else:
        return "Le nombre est plus petit. Essayez à nouveau."
    
def jeu_de_devinette():
    print("Bienvenue dans le jeu de devinette !")
    nombre_secret = generer_nombre_secret()
    essais_max = 5

    for essai in range(essais_max):
        tentative = int(input("Devinez le nombre (entre 1 et 100) : "))
        
        resultat = deviner_nombre(nombre_secret, tentative)
        print(resultat)

        if tentative == nombre_secret:
            print(f"Nombre d'essais : {essai + 1}")
            break
    else:
        print(f"Dommage ! Le nombre secret était {nombre_secret}")


jeu_de_devinette()