import os

def climat_ecologie(cleaned, word, word1):
    index = {}
    for filename in os.listdir(cleaned):
        with open(os.path.join(cleaned, filename), "r") as f:
            text = f.read()
            mots_texte = text.split() #converti chaque mot du texte d'un fichier et le garde dans une liste
            for i in range(0, len(mots_texte)): # parcour la liste du texte
                if word in mots_texte[i] or word1 in mots_texte: #execute l'action quand le mots est dans le texte
                    index = index.append(mots_texte[i]) #contient l'indexe de l'apparition du mot
                    break
                if

cleaned = "/path/to/cleaned"
word = "ecolocologie"
word1 = "climat"
climat_ecologie(cleaned, word)
for i in len(matrice):
    for j in len(matrice[i]):
        if matrice[i][j] >= 0 and matrice[i+1][j] >= 0:
            if matrice[i][j] <= matrice[i+1][j]:
                indexe = matrice[i][j]
            else:
                indexe = matrice
        elif matrice[i][j] <= 0 and matrice[i+1][j] >= 0:
            indexe = indexe(b)+#le split du fichier 1
        else:
            not found
