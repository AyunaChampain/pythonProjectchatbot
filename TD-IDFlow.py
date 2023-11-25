from TFIDF import *

TfIdf = TFIDF("./cleaned")
print(TfIdf)
min = 0

for i in range(len(TfIdf)) :
    s = 0
    for j in range(1,len(TfIdf[i])) :
        s += TfIdf[i][j]
    if s >= min :
        min = s
        mot = TfIdf[i][0]
print(mot)