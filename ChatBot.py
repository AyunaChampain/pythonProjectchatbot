# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot

from motsquestion import *
from reponsereturn import *
from qu5 import *
from tf_eleve_question import *
from affiner_rep import *

question = str(input("Bonjour cher utilisateur ! Je suis J.O.C., ChatBot à votre service, comment puis-je vous aider ? "))
question = mots_question(question)
tfidf = inverse_matr(TFIDF("./cleaned"))
TFIDF_qu = Tfidf(question)
files = list_of_files("./cleaned", 'txt')
doc = pertin(tfidf, TFIDF_qu, files)
mot = tfidf_question(question)
rep = repreturn(doc, mot)
if rep != "Désolé, je n'ai pas la réponse à votre question." :
    print(affin_rep(question, rep))
else :
    print(rep)
