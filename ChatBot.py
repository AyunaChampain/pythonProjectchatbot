# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot

from motsquestion import *
from reponsereturn import *
from qu5 import *
from tf_eleve_question import *

question = str(input("Bonjour cher utilisateur ! Je suis JOC, ChatBot à votre service, comment puis-je vous aider ? "))
question = mots_question(question)
tfidf = inverse_matr(TFIDF("./cleaned"))
TFIDF_qu = Tfidf(question)
files = list_of_files("./cleaned", 'txt')
doc = pertin(tfidf, TFIDF_qu, files)
mot = tfidf_question(question)
print(repreturn(doc, mot))
