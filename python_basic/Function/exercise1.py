# Exercice 1: Addition de deux nombres
# Écrivez une fonction appelée addition qui prend deux nombres en argument et renvoie leur somme.

def addition(*args):
    total = 0
    for nombre in args:
        total += nombre
    return total
    
print(addition(10,3))

