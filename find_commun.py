from Functions import *
tf = tf("./cleaned")
TfIdf = TFIDF("./cleaned")
mot = []

#liste pour ajouter tout les mots utilisés par chacun des présidents
tousmots = []
for i in tf[0] :
    compt = 0
    #parcour le dictionnaire
    for j in range (len(tf)) :
        if i in tf[j] :
            compt += 1
    #si le compteur = à 8 un des mots à étè utilisé dans chaque fichier, il est donc ajouté à une liste
    if compt == 8 :
        tousmots.append(i)
print("Les mots que tous les présidents ont prononcé sont : ", tousmots)

#Note : Les mots n'excluent pas les mots non-importants car tous les mots en commun prononcés par les présidents sont considérés comme non-important