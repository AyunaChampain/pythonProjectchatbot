
tets="je suis un gros canard gros"

#creer un dictionnaire vide
tf={}
#séparer chauqe mot du texte
mots=texte.split()
#ajouter dans le dictionnaire les mots s'il ne le sont pas déjà et indiquer leur occurence
for mot in mots:
    if mot not in tf:
        tf[mot]=1
    else:
        tf[mot] = tf[mot] + 1
print(tf)

