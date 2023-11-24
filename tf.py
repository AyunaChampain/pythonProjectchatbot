
from math import *
from os import listdir

def list_of_files(directory, extension):
    files_names = []
    for filename in listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def tf (repert) :
    dico = {}
    M = []
    list = list_of_files(repert, "txt")
    for i in range (len(list)) :
        L = []
        with open("./cleaned/" + list[i], "r") as f :
            Lignes = f.readlines()
    for discours in Lignes:
        #creer un dictionnaire vide
        tf={}
        #séparer chaque mot du texte
        mots=discours.split()
        #ajouter dans le dictionnaire les mots s'il ne le sont pas déjà et indiquer leur occurence
        for mot in mots:
            if mot not in tf:
                tf[mot]=1
            else:
                tf[mot] = tf[mot] + 1
        print(tf)

