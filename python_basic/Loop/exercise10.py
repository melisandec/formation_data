### Exercices de Chaînes de Caractères

# Palindrome Checker: Écrire un programme qui vérifie si une chaîne de caractères donnée est un palindrome ou non.

mot = "radar"
motreverse = mot[::-1]
print(motreverse)
if mot == motreverse :
    print("C'est un palindrome")


# Compter les Voyelles et les Consonnes: Donnée une chaîne de caractères, utiliser une boucle for 
# pour compter le nombre de voyelles et de consonnes.

example = "Count number of vowels in a String in Python"

# initializing count variable
count = 0

# declaring a variable for index
i = 0

# iterate over the given string (example)
# len(example) -> gives the length of the string in Python

for i in range(len(example)):
    if (
        (example[i] == "a")
        or (example[i] == "e")
        or (example[i] == "i")
        or (example[i] == "o")
        or (example[i] == "u")
    ):
        count += 1

print("Number of vowels in the given string is: ", count)