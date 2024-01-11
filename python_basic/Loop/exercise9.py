# Table de Multiplication: Utiliser des boucles for imbriquées pour afficher une table de multiplication 
# jusqu'à 10x10.

def table(nb, max=10):
    for i in range(1,max+1):
        print(i, " * ", nb, " = ", i * nb)
