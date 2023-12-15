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
    for i in range(len(tf_qu)) :
        tf_qu[i][1] /= len(quest)
    return tf_qu

def Tfidf(quest) :
    TF = tf_qu(quest)
    M = inverse_matr(TFIDF("./cleaned"))
    vecqu = []
    for i in range (len(M[0])) :
        vecqu.append("")
    for i in range (len(M)) :
        for j in range (len(M[i])) :
            vecqu[j] = (TF[i][1] * M[i][j])
    return vecqu