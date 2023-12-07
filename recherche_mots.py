#read fichier faire liste des mots
#en sortir une liste des mots
def recherche_mots():
    liste = []
    liste_commun = []
    with open("./cleaned/", 'r') as f1 :
        fichier_mots = f2.readlines()
        for i in fichier_mots:
            f_mots = i.split()
            Liste.append(f_mots)
    for j in range(len(liste)):
        if liste in mots_question:
            liste_commun.append(liste[i])
    return liste_commun