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
    print (M)


TFIDF("./cleaned")