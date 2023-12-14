# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot
# Fonction qui ressort la liste des président ayant mentionné "nation"
# Ressort le nom de celui l'ayant le plus mentionné
from Functions import *


M = []
repert = "./cleaned"
#Récupère les noms des fichiers
list = list_of_files(repert, "txt")
for i in range (len(list)) :
    L = []
    #Créer une matrice contenant des listes de mots
    with open("./cleaned/" + list[i], 'r') as f :
        contenu = f.readlines()
        for l in contenu:
            mots = l.split()
            L.append(mots)
    M.append(L)

prsdt = []
compteur = []

#Parcours les mots
for fichier in range (len(M)) :
    compt = 0
    verif = True
    for ligne in M[fichier] :
        #Vérifie si le mot 'nation' est compris dans la ligne
        if "nation" in ligne :
            #Compte un 'nation' supplémentaire
            compt += 1
            #Si le président n'a pas déjà dit ce mot, on ajoute son nom
            #dans une liste
            if verif == True :
                prsdt.append(fichier)
                verif = False
    #On garde le nombre de 'nation' dans une liste
    compteur.append(compt)
min = 0
for nbr in range(len(compteur)) :
    if compteur[nbr] > min :
        max = compteur[nbr]



L = noms()
nom = []
print("Les présidents ayant prononcé le mot nation sont : ", end = "")
for i in prsdt :
    if L[i] not in nom :
        nom.append(L[i])
for i in nom :
    print(i, end = " ")
print("")
print("Celui l'ayant le plus prononcé est : ", L[max])
