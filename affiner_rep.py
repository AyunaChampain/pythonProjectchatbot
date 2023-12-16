# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot
# Fonction permettant d'affiner une réponse avec des répliques en début de phrase.
# Ajoute des points en fin de phrase

def affin_rep(quest, repbr) :
    question_starters = {"comment": "Après analyse, ", "pourquoi": "Car, ", "peux tu": "Oui, bien sûr!"}
    x = quest[0]
    rep = ""
    nv_mot = ""
    if x in question_starters.keys() :
        for i, j in question_starters.items() :
            if i == x :
                rep = j
    for i in range(len(repbr[0])) :
        if i == 0 :
            rep += chr(ord(repbr[0][i]) - 32)
        else :
            rep += repbr[0][i]
    rep += "."
    return rep
