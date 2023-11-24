from tf import *
from IDF import *
def TFIDF (reper) :
    M = []
    #TF = tf(reper)
    idf = IDF(reper)
    print(idf)
    for mot in idf.keys() :
        L = []
        L.append(mot)
        M.append(L)
    """for j in range(len(TF)) :
            for i in range(len[M]) :
                M[i] = TF[j] * idf[i]
        print(M)"""



TFIDF("./cleaned")