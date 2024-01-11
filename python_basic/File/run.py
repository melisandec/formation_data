file = open("/Users/melisandecornetlichtfus/Desktop/Formation/python_basic/File/monfichier.txt","r")

print(file.read(5)) # Print 5 premier caracteres

# Lire un document entier
for each in file:
    print(each)

# Ecrire dans un document
file = open("/Users/melisandecornetlichtfus/Desktop/Formation/python_basic/File/monfichier.txt","w")

file.write("NOUS SOMMES EN FORMATION")
file.close()

# Transformer un element en liste 
animaux = "girafe:tigre:singe:souris"
print(animaux.split(":"))

# Transformer un element en liste 