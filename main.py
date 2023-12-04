from Functions import *


if __name__ == '__main__':

    print("Bonjour, bienvenue sur le ChatBot")
    print("Que souhaitez vous faire ? ")
    print("Tapez :")
    print("1 pour obtenir la liste des mots les moins importants.")
    print("2 pour les mots dont le score TD-IDF les plus élevés.")
    print("3 pour les mots les plus répétés par le président Chirac.")
    print("4 pour obtenir la liste des noms des présidents ayant parlé de Nation et celui qui a répété le plus de fois le mot Nation.")
    print("5 pour obtenir le nom du premier président à parler d'écologie.")
    print("6 pour obtenir les mots que tous les présidents ont prononcé.")
    choix = 0
    while choix < 1 or choix > 6 :
        choix = int(input("Choisissez une commande : "))
    print("")


    if choix == 1 :
        from TFIDFlow import *
        print("Les mots les moins importants (ayant le score TF-IDF le plus bas) sont : ", TFIDFLOW())
    if choix == 2 :
        from tfidfelevé import *
    if choix == 3 :
        from chiracmot import *
    if choix == 4 :
        from findpresidentnation import *
    if choix == 5 :
        from findecolo import *
    if choix == 6 :
        from find_commun import *

