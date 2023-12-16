# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot
# Matrice du TF et de l'IDF de la question
from Functions import *
from motsquestion import *

def tf_qu(quest) :
    tf_qu = []
    tfidf = TFIDF("./cleaned")
    for i in range(len(tfidf)) :
        tf_qu.append([tfidf[i][0], 0])
        for j in quest :
            if tfidf[i][0] == j :
                tf_qu[i][1] += 1
    return tf_qu

def Tfidf(quest) :
    TF = tf_qu(quest)
    M = IDF("./cleaned")
    vecqu = []
    for i in range (len(M)) :
        vecqu.append("")
    for i in range (len(M)) :
        vecqu[i] = (TF[i][1] * M[TF[i][0]])
    return vecqu

Tfidf(["nation"])