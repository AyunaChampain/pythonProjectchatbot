from math import *
from os import listdir


#Fonction permettant de lire les noms des différents fichiers
#contenus dans un répertoire
def list_of_files(directory, extension):
    files_names = []
    for filename in listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

#Fonction affichant la liste des présidents
def nompresident(noms_prsdt):
    Listepres=[]
    #cpt pour n'afficher que la première occurence
    cpthollande = 0
    cptchirac = 0
    cptgiscard = 0
    cptmacron = 0
    cptsarkozy = 0
    cptmitterrand = 0
    #Ajoute les noms dans la liste pour qu'elle soit envoyée plus tard
    for nom in noms_prsdt:
        if nom == 'Chirac' and cptchirac == 0 :
            Listepres.append(nom)
            #Lorsque le nom est ajouté une première fois dans la liste, cpt ne prend plus la valeur de 0
            cptchirac = 1
        elif nom == 'Mitterrand' and cptmitterrand == 0 :
            Listepres.append(nom)
            cptmitterrand = 1
        elif nom == 'Hollande' and cpthollande == 0 :
            Listepres.append(nom)
            cpthollande = 1
        elif nom == 'Macron' and cptmacron == 0 :
            Listepres.append(nom)
            cptmacron = 1
        elif nom == 'Sarkozy' and cptsarkozy == 0 :
            Listepres.append(nom)
            cptsarkozy = 1
        elif nom == 'Giscard dEstaing' and cptgiscard == 0 :
            Listepres.append(nom)
            cptgidcard = 1
    return Listepres


#Fonction isolant le nom du président du nom du fichier
def noms() :
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")

    noms_prsdt = []
    for nom_f in files_names : #nom_f = noms fichiers
        nom = ""
        for lettre in range (11, len(nom_f)-4): #Parcours chaque lettre du nom hors "Noination_" et l'extension
            if ord(nom_f[lettre]) <= 48 or ord(nom_f[lettre]) >= 57 : #verifie que le charactère n'est pas un chiffre
                nom += nom_f[lettre]
        noms_prsdt.append(nom)
    return noms_prsdt


#Permet de transformer tous le contenu des fichiers en minuscules
def minuscules(repert) :
    list = list_of_files(repert, "txt")
    for i in range (len(list)) :
        with open("./speeches/" + list[i], 'r') as f :
            contenu = f.readlines()
            for line in contenu :
                new_line = ""
                for cara in line :
                    if ord(cara) >= 65 and ord(cara) <= 90 :
                        new_line += chr(ord(cara) + 32)
                    else :
                        new_line += cara
                with open("cleaned/" + list[i], "a") as f2 :
                    f2.write(new_line)


#Retire la ponctuation et tout caractère spécial des textes
def ponctuation(reper):
    dico = {}
    M = []
    list = list_of_files(reper, "txt")
    for i in range(len(list)):
        new_line2 = ""
        with open("./cleaned/" + list[i], 'r') as f3:
            contenu2 = f3.readlines()
            for lines in contenu2 :
                for cara2 in lines :
                    if (ord(cara2) >= 33 and ord(cara2) <= 38) or (ord(cara2) >= 40 and ord(cara2) <= 44) or (ord(cara2) >= 46 and ord(cara2) <= 47) or (ord(cara2) >= 58 and ord(cara2) <= 63) or (ord(cara2) >= 91 and ord(cara2) <= 96) or (ord(cara2) >= 123 and ord(cara2) <= 126):
                        new_line2 += " "
                    elif (ord(cara2) == 39) or (ord(cara2) == 45):
                        new_line2 += " "
                    else:
                        new_line2 += cara2
            with open("./cleaned/" + list[i], "w") as f4 :
                f4.write(new_line2)


#Calcule le tf
def tf (repert) :
    L = []
    list = list_of_files(repert, "txt")
    for i in range (len(list)) :
        with open("./cleaned/" + list[i], "r") as f :
            #lit chaque discours séparément
            Lignes = f.readlines()
                #crée un dictionnaire vide
            tf={}
            for l in Lignes:
                #sépare chaque mot du texte
                mots = l.split()
                #ajouter dans le dictionnaire les mots s'ils ne le sont pas déjà
                for mot in mots:
                    if mot not in tf and mot != " " and mot != "" :
                        tf[mot]=1
                    # incrémente la valeur dans le dictionnaire à chaque fois que le mot réapparaît
                    else:
                        tf[mot] = tf[mot] + 1
            #ajoute le dictionnaire dans la liste
            L.append(tf)
    return L


#Calcule l'IDF
def IDF (repert) :
    dico = {}
    M = []
    list = list_of_files(repert, "txt")
    TF = tf("./cleaned")
    for i in range (len(list)) :
        L = []
        with open("./cleaned/" + list[i], "r") as f :
            Lignes = f.readlines()
        for l in Lignes :
            mot = ""
            mots = l.split()
            for i in mots :
                L = []
                L.append (i)
                M.append(L)
    dico = {}
    for i in M :
        cpt = 0
        for mot in i :
            for j in TF :
                if mot in j.keys() :
                    cpt += 1
        dico[mot] = cpt
    for i in dico.keys() :
        dico[i] = log10(len(list)/dico[i])
    return dico


#Calcule le score TF-IDF
def TFIDF (reper) :
    M = []
    TF = tf(reper)
    idf = IDF(reper)
    for mot in idf.keys() :
        L = []
        if mot != "" :
            L.append(mot)
            M.append(L)
    for j in range(len(TF)) :
        for i in range(len(M)) :
            if M[i][0] in TF[j].keys() :
                M[i].append(TF[j][M[i][0]] * idf[M[i][0]])
    return M
