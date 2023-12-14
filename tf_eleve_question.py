from score_qu import *
from motsquestion import *
tf_question = tf_qu(quest)
def tfidf_question():
    eleve = 0
    place = 0
    mot_question = " "
    for i in len(tf_question):
        if tf_question[i] >= eleve:
            eleve = tf_question[i]
            place = i
    mot_question = listedesmots[place]
    return mot_question