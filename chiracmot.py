def chiracrepet(tfidf, listemots):
    max_tfidf = 0
    lemotenquestion =""
    #parcourir la ligne de la matrice
    for i in range(len(tfidf)):
        #parcourir colone de la matrice
        for j in range(len(tfidf[i])):
            ## Vérifier si le score tf idf est plus grand que le maximum actuel
            if tfidf[i][j] > max_tfidf:
                max_tfidf = tfidf[i][j]
                lemotenquestion= listemots[i]
return lemotenquestion

#à mettre dans main
# motplusgrandtfidf = chiracrepet(tfidf, listemots)