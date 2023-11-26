from Functions import *
def chiracrepet(tfidf):
    max_tfidf = 1
    mot =""
    #parcourir la ligne de la matrice
    for i in range(len(tfidf)):
        #parcourir colone de la matrice
        for j in range(1,2):
            ## Vérifier si le score tf idf est plus petit que le maximum actuel
            if tfidf[i][j] < max_tfidf:
                max_tfidf = tfidf[i][j]
                mot =tfidf [i][0]
    return mot



"""tfidf = TFIDF("./cleaned")
listemots = ""
print(chiracrepet(tfidf, listemots))"""