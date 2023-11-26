from Functions import *
def chiracrepet(tfidf):
    max_tfidf = 0
    mot =""
    #parcourir la ligne de la matrice
    for i in range(len(tfidf)):
        #parcourir colone de la matrice
        for j in range(2,3):
            ## Vérifier si le score tf idf est plus grand que le maximum actuel
            if tfidf[i][j] > max_tfidf:
                max_tfidf = tfidf[i][j]
                mot =tfidf [i][1]
    return mot


tfidf = TFIDF("./cleaned")
listemots = ""
print(chiracrepet(tfidf, listemots))