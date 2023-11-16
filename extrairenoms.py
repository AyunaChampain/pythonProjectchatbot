import os


#Fonction qui extrait le nom des fichiers
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names



#Affiche uniquement les noms
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
    print(noms_prsdt)

noms()
