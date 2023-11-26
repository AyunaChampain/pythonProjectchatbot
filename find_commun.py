def commun(M):
    # Trouver les mots que tous les présidents ont utilisés
    mots_communs = []
    for i in range(len(matrice[0])):
        mot_present = True
        for j in range(1, len(matrice)):
            if matrice[j][i] == 0:
                mot_present = False
                break
        if mot_present:
            mots_communs.append(i)
    return mots_communs

from Functions import *
tf = tf("./cleaned")
TfIdf = TFIDF("./cleaned")
mot = []


tousmots = []
for i in tf[0] :
    compt = 0
    for j in range (len(tf)) :
        if i in tf[j] :
            compt += 1
    if compt == 8 :
        tousmots.append(i)
print(tousmots)

#Note : Les mots n'excluent pas les mots non-importants car tous les mots en commun prononcés par les présidents sont considérés comme non-important