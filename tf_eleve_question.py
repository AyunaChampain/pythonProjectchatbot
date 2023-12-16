# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot
# Fonction qui retourne le mot avec le TF-IDF le plus élevé dans la question
from score_qu import *
from motsquestion import *
from Functions import *


def tfidf_question(quest):
    tfidf_qu = Tfidf(quest)
    eleve = 0
    place = 0
    for i in range(len(tfidf_qu)):
        if tfidf_qu[i] >= eleve:
            eleve = tfidf_qu[i]
            max = i
    liste = listetoutmots()
    return liste[max]
