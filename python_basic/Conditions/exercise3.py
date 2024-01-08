#qui demande à l'utilisateur de saisir une note entre 0 et 100. En fonction de la note, affichez la mention correspondante selon les règles suivantes :

# 0-40 : "Échec"
# 41-60 : "Passable"
# 61-75 : "Assez bien"
# 76-90 : "Bien"
# 91-100 : "Très bien"

note = int(input("Entrer note entre 0 et 100: "))
if note <= 40 :
    print("Échec")
elif note <= 60:
    print("Passable")
elif note <= 75:
    print("Assez bien")
elif note <= 91:
    print("Bien")
else:
    print("Très bien")
