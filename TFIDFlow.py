from Functions import *

TfIdf = TFIDF("./cleaned")
min = 0
mot = []

#Parcours la matrice TfIdf
for i in range(len(TfIdf)) :
    #Intialise la moyenne des scores à 0
    s = 0
    #Calcule la moyenne des scores TfIdf de chaque mot
    for j in range(1,len(TfIdf[i])) :
        s += TfIdf[i][j]
    s /= len(TfIdf[i])
    #Garde les mots dont le score est inférieur à 0.35
    if s <= 0.35 :
        min = s
        mot.append(TfIdf[i][0])


print("Les mots les moins importants (ayant le score TF-IDF le plus bas) sont : ",mot)