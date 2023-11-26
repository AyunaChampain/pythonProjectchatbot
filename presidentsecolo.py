import os
def ecologie_climat(mots, liste_files):
    index = -1
    liste_index = []
    indices_president = {}
    for filenoms in liste_files: #le nom de la liste des presidents
        # Vérifier si le fichier existe
        if os.path.isfile(filenoms):
            # Lire le contenu du fichier
            with open(filenoms, 'r', encoding='utf-8') as file: #changer le with??
                texte = file.read().split() #créer une liste des mots des fichiers
    for i in len(texte): #parcour les element de la liste
        if texte[i] in mots: #vérifie si le mot et un des deux mots cherché
            index = i
            liste_index = liste_index.append(i) #ajoute à une liste a quelle indexe un des mots et apparus
            indices_president[filenoms] = index
            break #??
