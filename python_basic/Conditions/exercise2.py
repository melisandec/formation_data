### calculer le cout d'un trajet en taxi. Si le trajet fait 
# 0 à 10 km : 5€
# 11 à 30 km : 10€
# Plus de 30 km : 15€
km = int(input("Entrer nombre de km: "))
if km <=10 :
    print("5€")
elif km <30 :
    print("10€")
else :
    print("15€")
