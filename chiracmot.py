from Functions import *
tf = tf("./cleaned")

clemax = 0
motmax = ''
#parcours les dictionnaires dans la liste
for a in range (len(tf)):
    #parcours seulement les dictionnaires liés au président Chirac
    if tf[a] == tf[0] or tf[a] == tf[1]:
        #parcours les mots de chaque dossiers
        for cle in tf[a].keys():
            #trouve le mot ayant été dit le plus de fois
            if tf[a][cle] > clemax:
                clemax = tf[a][cle]
                motmax = cle

print('Le mot ayant été le plus répété par le président Chirac est :',motmax)



