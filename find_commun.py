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
print("Les mots que tous les présidents ont prononcé sont : ", tousmots)

#Note : Les mots n'excluent pas les mots non-importants car tous les mots en commun prononcés par les présidents sont considérés comme non-important