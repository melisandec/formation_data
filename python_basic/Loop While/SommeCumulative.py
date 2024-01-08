# Exercice 1 : Somme cumulative
# Écrivez un programme qui demande à l'utilisateur d'entrer des nombres jusqu'à ce 
# qu'il entre un nombre négatif. Ensuite, le programme affiche la somme cumulative des nombres saisis.

list_ = list()
while (n := int(input("Enter a number, put in a negative number to end: "))) >= 0:
    list_.append(n)
print('Sum of number entered: ', sum(list_))
