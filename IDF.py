from math import *
from os import listdir
from extrairenoms import *


def IDF (repert) :
    dico = {}
    M = []
    list = list_of_files(repert, "txt")
    for i in range (len(list)) :
        L = []
        with open("./cleaned/" + list[i], "r") as f :
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
        dico[i] = log10(1 + (len(list)/dico[i]))
    return dico