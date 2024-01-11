### Devine le nombre

# Générez un nombre aléatoire entre 1 et 100. Ensuite, demandez à l'utilisateur de deviner le nombre. 
# Donnez des indices (plus grand ou plus petit) jusqu'à ce que l'utilisateur trouve le bon nombre. 
# Affichez le nombre d'essais nécessaires à la fin.

from random import randint

num = randint(1, 100)  # Stores the random number between 1 and 100 in the variable 'number'.
guess = None

while guess != num :
    guess = input("Deviner un chiffre entre 1 and 100: ")
    guess = int(guess)
    if guess == num:
          print("Bravo!")
          print("Les nombre est: ",num)
          break
    elif guess > num:
         print("plus petit")
    else :
         print("plus grand")



