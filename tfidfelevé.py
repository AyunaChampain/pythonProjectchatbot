# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot
#obtenir le score TD-IDF le plus élevé pour chaque document.
from Functions import *



def tfidf_eleve(tfidf):
    #Initialisation du maximum à 0
    maxi_tfidf = 0
    #parcourir la ligne de la matrice
    for i in range(len(tfidf)):
        #parcourir colone de la matrice
        for j in range(1, len(tfidf[i])):
            #Comparer le maximum à la valeur
            if tfidf[i][j] > maxi_tfidf:
                maxi_tfidf = tfidf[i][j]
                mot = tfidf[i][0]
    return mot


tfidf = TFIDF("./cleaned")
print("Le mot ayant le tf-idf le plus élevé est : ", tfidf_eleve(tfidf))
