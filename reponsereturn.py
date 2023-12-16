# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot
# Fonction qui retourne la phrase contenant la première occurence du mot au TF-IDF le plus élevé dans le bon document
from Functions import *

def repreturn(docpertinent,motquestioneleve):
    a = []
    with open("./cleanedpoint/" + docpertinent,"r") as docpertinent:
        lignes = docpertinent.readlines()
        for i in lignes :
            ligne = i.replace("-",".")
            ligne = i.replace("!",".")
            ligne = i.replace("?",".")
            a.append(ligne.split("."))
        cpt = 0
        for sentence in a:
            phrase = sentence[0].split(" ")
            if motquestioneleve in phrase :
                return sentence
    return "Désolé, je n'ai pas la réponse à votre question."