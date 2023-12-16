# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot
# Ressort le fichier le plus pertinent
from score_qu import *
from Functions import *
from motsquestion import *

def pertin(tfidf, TFIDF_qu, files) :
    max = 0
    for i in range (len(tfidf)) :
        a = sim(tfidf[i], TFIDF_qu)
        if a >= max :
            max = a
            nom = files[i]
    return nom
