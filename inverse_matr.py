from Functions import *

def inverse_matr(M) :
    M2 = []
    for j in range (1, len(M[0])-1) : #colonnes
        L = []
        for i in M : #parcours les lignes
            print(i)
            L.append(i[j])
        M.append(L)
    print(M)

inverse_matr(TFIDF("./cleaned"))