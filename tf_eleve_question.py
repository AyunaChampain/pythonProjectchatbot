# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot
# Fonction qui retourne le mot avec le TF-IDF le plus élevé dans la question
from score_qu import *
from motsquestion import *


def tfidf_question(quest):
    tf_question = tf_qu(quest)
    eleve = 0
    place = 0
    for i in range(len(tf_question)):
        if tf_question[i] >= eleve:
            eleve = tf_question[i]
            place = i
    motquestioneleve = listedesmots[place]
    return motquestioneleve
