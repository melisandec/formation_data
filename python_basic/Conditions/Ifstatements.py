# ecriver un programe qui demande à l'utilisateur d'écrire un nombre entier pour voir si la réponse est pair ou impair.
nombre = int(input("Entrer nombre entier:"))
if nombre % 2 == 0:
    print("pair")
else :
    print("impair")