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
#commencer par 1 et 1 dans colonne et ligne
#dans chaque ligne verifier si tout les tf sont au dessus de 0 si oui les mettre dans une liste
mots_communs = []
for i in range(1, len(M)):
    mot_present = True
    for j in range(1, len(M[i])):
        if M[i][j] <= 0:
            mot_present = False
            break
    if mot_present:
        mots_communs.append(i)
print(f"Les mots qui sont dans chaque fichier sont: {mots_communs}")
