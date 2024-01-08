# Somme des N Premiers Nombres: 
# Utiliser une boucle pour calculer la somme des n premiers nombres, où n est
# un nombre entré par l'utilisateur.

n = int(input("Entrez n : "))
somme = sum(range(n + 1))
print(somme)