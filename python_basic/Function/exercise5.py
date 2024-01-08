# Exercice 5: Vérification de palindrome
# Écrivez une fonction appelée est_palindrome qui prend une chaîne de caractères en argument 
# et renvoie True si la chaîne est un palindrome, False sinon.

def palindrome(mot):
    reverse = mot[::-1]
    if mot == reverse :
        print(True)
    else:
        print(False)

palindrome("house")
