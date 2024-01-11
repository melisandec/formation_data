# Filtrer les Nombres: Étant donné une liste de nombres, 
# utiliser une boucle for pour créer une nouvelle liste contenant uniquement 
# les nombres supérieurs à un certain seuil.
liste_nombres = [1,2,3,4,5,7,8,11,15,16,23,36,78]
nombres_filtrer = []

for n in liste_nombres :
    if n > 9 :
        nombres_filtrer.append(n)
print(nombres_filtrer)