# This is a sample Python script.
from Minuscules import *
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
if __name__ == '__main__':

    print("Bonjour, bienvenue sur le ChatBot")
    print("Que souhaitez vous faire ? ")
    print("Tapez :")
    print("1 pour obtenir la liste des mots les moins importants.")
    print("2 pour les mots dont le score TD-IDF les plus élevés.")
    print("3 pour les mots les plus répétés par le président Chirac.")
    print("4 pour obtenir la liste des noms des présidents ayant parlé de Nation et celui qui a répété le plus de fois le mot Nation.")
    print("5 pour obtenir le nom du premier président à parler d'écologie.")
    print("6 pour obtenir les mtos que tous les présidents ont prononcé.")
    choix = 0
    while choix < 1 or choix > 5 :
        choix = input("Choisissez une commande : ")