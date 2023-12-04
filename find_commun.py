from Functions import *
from TFIDFlow import TFIDFLOW

tf = tf("./cleaned")
TfIdf = TFIDF("./cleaned")
mot = []

#liste pour ajouter tout les mots utilisés par chacun des présidents
tousmots = []
non_imp = TFIDFLOW()
for i in tf[0] :
    compt = 0
    #parcour le dictionnaire
    for j in range (len(tf)) :
        if i in tf[j] :
            compt += 1
    #si le compteur = à 8 un des mots à été utilisé dans chaque fichier, il est donc ajouté à une liste
    if compt == 8 and i not in non_imp :
        tousmots.append(i)
print("Les mots que tous les présidents ont prononcé sont : ", tousmots)

#Note : Les mots n'excluent pas les mots non-importants car tous les mots en commun prononcés par les présidents sont considérés comme non-important