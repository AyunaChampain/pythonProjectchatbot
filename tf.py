
from math import *
from os import listdir

def list_of_files(directory, extension):
    files_names = []
    for filename in listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def tf (repert) :
    L = []
    list = list_of_files(repert, "txt")
    for i in range (len(list)) :
        with open("./cleaned/" + list[i], "r") as f :
            #lire chaque discours séparément
            Lignes = f.readlines()
                #creer un dictionnaire vide
            tf={}
            for l in Lignes:
                #séparer chaque mot du texte
                mots = l.split()
                #ajouter dans le dictionnaire les mots s'ils ne le sont pas déjà et indiquer leur occurence
                for mot in mots:
                    if mot not in tf and mot != " " and mot != "" :
                        tf[mot]=1
                    else:
                        tf[mot] = tf[mot] + 1
            L.append(tf)
    return L