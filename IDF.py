from math import *
from os import listdir

def list_of_files(directory, extension):
    files_names = []
    for filename in listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def IDF (repert) :
    dico = {}
    M = []
    list = list_of_files(repert, "txt")
    for i in range (len(list)) :
        L = []
        with open("./speeches/" + list[i], "r") as f :
            Lignes = f.readlines()
        for l in Lignes :
            mot = ""
            for lettre in l :
                if lettre == " " :
                    if mot not in L :
                        L.append(mot)
                    mot = ""
                else :
                    mot += lettre
        if mot not in L :
            L.append(mot)
        M.append(L)
    dico = {}
    for i in M :
        for mot in i :
            if mot not in dico.keys() :
                dico[mot] = 1
            else :
                dico[mot] = dico[mot] + 1
    for i in dico.keys() :
        dico[i] = log(len(list)/dico[i])
    print(dico)
IDF("./speeches")