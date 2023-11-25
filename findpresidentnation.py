def findpresident(tfidf,listemots,listedoc):
    #trouver l'index du mot

    index_mot = listemots.index("Nation")

    max_score = 0
    max_index = 0
    #liste pour stocker tous les présidents qui ont parlé de Nation
    presidents=[]

    #parcourir les documents à l'index du mot nation
    for i in range(len(tfidf[index_mot])):
            if tfidf[index_mot][i] > 0:
                presidents.append(listedoc[i])
                #pour mettre l'index et la valeur du plus grand tf-idf
            if tfidf[index_mot][i] > max_score:
                max_score = tfidf[index_mot][i]
                max_index = i
    #mettre le président qui a le plus répété le mot
    president_final = listedoc[i]

    return presidents, president_final

# à mettre dans main
# lespresidents,president_most_repeat = findpresident(tfidf,listemots,listedoc)