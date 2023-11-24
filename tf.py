from math import *
from os import listdir

def list_of_files(directory, extension):
    files_names = []
    for filename in listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def tf (repert) :
    #creer un dictionnaire vide
    tf={}
    #séparer chaque mot du texte
    mots=test.split()
    #ajouter dans le dictionnaire les mots s'il ne le sont pas déjà et indiquer leur occurence
    for mot in mots:
        if mot not in tf:
            tf[mot]=1
        else:
            tf[mot] = tf[mot] + 1
    return tf

