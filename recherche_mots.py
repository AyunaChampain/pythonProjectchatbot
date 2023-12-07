#read fichier faire liste des mots
#en sortir une liste des mots
mots_question = ["est", "ce", "que", "nn"]
def recherche_mots():
    Liste = []   #liste pour ajouter les mots du texte // sauf si y'en a deja une??
    liste_commun = []
    with open("./cleaned/", 'r') as f2:
        fichier_mots = f2.readlines()
        for i in fichier_mots:
            f_mots = i.split()
            Liste.append(f_mots)
    for j in range(len(Liste)): #parcour liste de tout les mots
        if Liste[j] in mots_questions:
            liste_commun.append(liste[i])   #on fait la liste des communs
    return liste_commun