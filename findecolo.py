# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot

from Functions import *
M = []
repert = "./cleaned"

#Récupère les noms des fichiers et sépare les mots en listes
list = list_of_files(repert, "txt")
for i in range (len(list)) :
    L = []
    with open("./cleaned/" + list[i], 'r') as f :
        contenu = f.readlines()
        for l in contenu:
            mots = l.split()
            L.append(mots)
    M.append(L)

L = []

#Parcours les mots
for discours in M :
    compt = 0
    rang = 0
    for ligne in range(len(discours)) :
        for mot in discours[ligne] :
            #Vérifie si le mot évoque l'écologie
            if mot == "écologie" or mot == "climat" or mot == "écologique" or mot == "climatique" :
                #Compte à quel rang dans le discours le mot a été prononcé
                rang = compt
            else :
                compt += 1
    L.append(rang)

#Retrouve le président qui a pononcé le mot le plus tôt
min = L[0]
liste = []
for rang in range (len(L)) :
    if L[rang] <= min and L[rang] != 0 :
        premier = rang
        liste.append(rang)
    else :
        min = L[rang + 1]

L = noms()
print("Les président à parler d'écologie sont : ", end = "")
for i in liste :
    print(L[i], end = " ")
print("")
print("Le premier président à en parler est : ", L[premier])


