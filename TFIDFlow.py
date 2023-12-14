# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot
# Fonction qui affiche les mots au score TF-IDF de 0

from Functions import *


def TFIDFLOW( ) :
    TfIdf = TFIDF("./cleaned")
    mot = []

    #Parcours la matrice TfIdf
    for i in range(len(TfIdf)) :
        #Intialise la moyenne des scores à 0
        s = 0
        #Calcule la moyenne des scores TfIdf de chaque mot
        for j in range(1,len(TfIdf[i])) :
            s += TfIdf[i][j]
        #Garde les mots dont le score est de 0
        if s == 0 :
            mot.append(TfIdf[i][0])
    return mot
