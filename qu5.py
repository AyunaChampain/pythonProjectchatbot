# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot

from score_qu import *
from Functions import *

def pertin(tfidf, TFIDF_qu, files) :
    max = 1
    for i in range (len(tfidf)) :
        a = sim(tfidf[i], TFIDF_qu[i])
        max =


tfidf = inverse_matr(TFIDF("./cleaned"))
TFIDF_qu = Tfidf(["messieurs", "messieurs"])
files = list_of_files("./cleaned", 'txt')
pertin(tfidf, TFIDF_qu, files)