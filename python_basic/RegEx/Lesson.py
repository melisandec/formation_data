### RegEX 

# Import re
import re

# re.findall
text = "Bonjour voici mon numero 06 14 54 23 45"
numbers = re.findall('[0-9]+',text)
print (numbers)

# re.search
animaux = "girafe tigre singe"
resultat = re.search("tigre",animaux)
print(resultat)

# Utiliser regEx pour remplacer un mot par un nouveau mot

def replace_word(texte,mot_remplacer,nouveau_mot):
      """Function pour remplacer mot dans un texte par un nouveau mot"""
      nouveau_texte = re.sub(r'\b'+re.escape(mot_remplacer)+ r'\b', nouveau_mot,texte)
      return nouveau_texte

texte_original = "la programmation python est geniale. python est trop puissant ! "
print(texte_original)
mot_a_modifier = 'python'
nouveau_mot = 'javascript'

texte_modifier = replace_word(texte_original,mot_a_modifier,nouveau_mot)
print(texte_modifier)


