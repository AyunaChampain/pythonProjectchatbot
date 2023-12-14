# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot

from Functions import *
from motsquestion import *

def tf_qu(quest) :
    tf_qu = []
    tfidf = TFIDF("./cleaned")
    for i in range(len(tfidf)) :
        tf_qu.append([tfidf[i][0], 0])
        for j in quest :
            print(j)
            if tfidf[i][0] == j :
                tf_qu[i][1] += 1
                print("ok")
    for i in range(len(tf_qu)) :
        tf_qu[i][1] /= len(quest)
    print(tf_qu)
    return tf_qu

def Tfidf(quest) :
    TF = tf_qu(quest)
    M = inverse_matr(TFIDF("./cleaned"))
    for i in range (len(M)) :
        for j in M[i] :
            j *= TF[i][1]
    return M

question = input()
Tfidf(mots_question(question))