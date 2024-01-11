# Les Collections 
#Compter les occurrences: donnée une  liste de mots, utiliser une boucle for 
# pour compter combien de fois chaque mot apparaît dans la liste.


mot_chercher = "sac"
compteur = 0
mots = ["sac","sac","veste","sac","veste","t-shirt","sac"]
for x in mots: 
        if x == mot_chercher:
            compteur += 1
            
print(compteur)

