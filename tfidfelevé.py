from Functions import *

#pour obtenir la liste des mots dans l’ordre dans lequel ils apparaissent dans la matrice TD-IDF.
#obtenir le score TD-IDF le plus élevé pour chaque document.


def tfidf_eleve(tfidf):
    maxi_tfidf2 = 0
    #parcourir la ligne de la matrice
    for i in range(len(tfidf)):
        #parcourir colone de la matrice
        for j in range(1, len(tfidf[i])):
            if tfidf[i][j] > maxi_tfidf2:
                maxi_tfidf2 = tfidf[i][j]
                mot = tfidf[i][0]
    return mot


tfidf = TFIDF("./cleaned")
print(tfidf_eleve(tfidf))