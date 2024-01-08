# Exercice 4: Calcul de la moyenne
# Écrivez une fonction appelée moyenne qui prend une liste de nombres en argument et renvoie leur moyenne.

def moyenne(*args):
    """donner la moyenne d'une liste de nombres"""
    moyenne = sum(args)/len(args)
    return(moyenne)

print(moyenne(4,6,2,9,7))
