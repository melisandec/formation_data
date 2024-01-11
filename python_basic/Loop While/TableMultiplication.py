### Table de multiplication
# Demandez à l'utilisateur d'entrer un nombre, puis affichez la table de multiplication 
# de ce nombre de 1 à 10 à l'aide d'une boucle while

number = int(input ("Entrer un nombre pour afficher sa table de multiplication: "))
count = 1

print ("La table de multiplication de ", number)
while count <= 10:
    number = number * 1
    print (number, "x", count, "=", number * count)    
    count += 1    
