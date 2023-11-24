from tf import *
from IDF import *
def TFIDF (reper) :
    M = []
    TF = tf(reper)
    idf = IDF(reper)
    print(TF)
    print(idf)
    for mot in idf.keys() :
        L = []
        if mot != "" :
            L.append(mot)
            M.append(L)
    print(M)
    for j in range(len(TF)) :
        for i in range(len(M)) :
            if M[i][0] in TF[j].keys() :
                M[i].append(TF[j][M[i][0]] * idf[M[i][0]])
        print(M)



TFIDF("./cleaned")