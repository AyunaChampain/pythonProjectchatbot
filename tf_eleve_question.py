# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot
from score_qu import *
from motsquestion import *
listedesmots = mots_question(question)
tf_question = tf_qu(quest)
def tfidf_question():
    eleve = 0
    place = 0
    for i in range(len(tf_question)):
        if tf_question[i] >= eleve:
            eleve = tf_question[i]
            place = i
    motquestioneleve = listedesmots[place]
    return motquestioneleve