from Functions import *

TfIdf = TFIDF("./cleaned")
mot = []

#Parcours la matrice TfIdf
for i in range(len(TfIdf)) :
    #Intialise la moyenne des scores à 0
    s = 0
    #Calcule la moyenne des scores TfIdf de chaque mot
    for j in range(1,len(TfIdf[i])) :
        s += TfIdf[i][j]
    #Garde les mots dont le score est inférieur à 0.38
    if s == 0 :
        mot.append(TfIdf[i][0])


print("Les mots les moins importants (ayant le score TF-IDF le plus bas) sont : ",mot)