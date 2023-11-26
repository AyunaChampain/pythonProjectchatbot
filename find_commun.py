def commun(M):
    # Trouver les mots que tous les présidents ont utilisés
    mots_communs = []
    for i in range(len(matrice[0])):
        mot_present = True
        for j in range(1, len(matrice)):
            if matrice[j][i] == 0:
                mot_present = False
                break
        if mot_present:
            mots_communs.append(i)
    return mots_communs
# Trouver le président qui a utilisé le mot le plus
presidents = {}
for mot in mots_communs:
    max_tfidf = 0
    for i in range(len(M)):
        if M[i][mot] > max_tfidf:
            max_president = i
            max_tfidf = M[i][mot]
    presidents[mot] = max_president
