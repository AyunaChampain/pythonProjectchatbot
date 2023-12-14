# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot

# Le programme contenu dans ce fichier permet de chercher les mots
# les plus répétés par le président Chirac lors de ses discours

from Functions import *
from TFIDFlow import *


tf = tf("./cleaned")
clemax = 0
motmax = []
non_imp = TFIDFLOW()
#parcours les dictionnaires dans la liste
for a in range (len(tf)):
    #parcours seulement les dictionnaires liés au président Chirac
    if tf[a] == tf[0] or tf[a] == tf[1]:
        #parcours les mots de chaque dossiers
        for cle in tf[a].keys():
            #trouve le mot ayant été dit le plus de fois
            if tf[a][cle] > clemax and cle not in non_imp and len(cle) > 1 :
                clemax = tf[a][cle]
                motmax.append(cle)

print('Les mots ayant été le plus répétés par le président Chirac sont :',motmax)



