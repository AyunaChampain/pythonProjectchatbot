from TFIDF import *

TfIdf = TFIDF("./cleaned")
min = 0
mot = []
print(TfIdf)

for i in range(len(TfIdf)) :
    s = 0
    for j in range(1,len(TfIdf[i])) :
        s += TfIdf[i][j]
    s /= len(TfIdf[i])
    print(s)
    if s <= 0.35 :
        min = s
        mot.append(TfIdf[i][0])
print(mot)