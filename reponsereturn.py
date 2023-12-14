# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot
# Fonction qui retourne la phrase contenant la première occurence du mot au TF-IDF le plus élevé dans le bon document
def repreturn(docfichier,motquestioneleve):
    with open("docfichier","w") as docpertinent:
        docpertinent = docpertinent.replace("-",".")
        docpertinent = docpertinent.replace("!",".")
        docpertinent = docpertinent.replace("?",".")
        a = docpertinent.split(".")
        cpt = 0
        for sentence in a:
            if motQuestionEleve in a and cpt == 0:
                cpt = 1
                return a




