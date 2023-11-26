from Functions import *
M = []
repert = "./cleaned"
list = list_of_files(repert, "txt")
for i in range (len(list)) :
    L = []
    with open("./cleaned/" + list[i], 'r') as f :
        contenu = f.readlines()
        for l in contenu:
            mots = l.split()
            L.append(mots)
    M.append(L)

prsdt = []
compteur = []
for fichier in range (len(M)) :
    compt = 0
    verif = True
    for ligne in M[fichier] :
        if "nation" in ligne :
            compt += 1
            if verif == True :
                prsdt.append(fichier)
                verif = False
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