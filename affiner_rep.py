# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot
# Fonction permettant d'affiner une réponse avec des répliques en début de phrase.
# Ajoute des points en fin de phrase

def affin_rep(quest) :
    question_starters = {"Comment": "Après analyse, ", "Pourquoi": "Car, ", "Peux-tu": "Oui, bien sûr!"}
    x = quest[0]
    rep = ""
    if x in question_starters.keys() :
        for i, j in question_starters.items() :
            if i == x :
                rep = j
    return rep
