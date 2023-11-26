def moins_important():
    LMoinsImportant = []
    nulle = 0
    MoinsRepete = ""
    #parcourir la ligne de la matrice
    for i in range(len(tfidf)):
        #parcourir colone de la matrice
        for j in range(len(tfidf[i])):
            ## Vérifier si le score tf idf est plus grand que le maximum actuel
            if tfidf[i][j] == nulle:
                LMoinsImportant = LMoinsImportant.append(listemots[i]) #.append(tfidf[i][0])
                MoinsRepete = listemots[i]
    return LMoinsImportant