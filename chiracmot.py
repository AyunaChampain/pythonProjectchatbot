from Functions import *
tf = tf("./cleaned")

clemax = 0
motmax = ''
for a in range (len(tf)):
    if tf[a] == tf[0] or tf[a] == tf[1]:
        for cle in tf[a].keys():
                if tf[a][cle] > clemax:
                    clemax = tf[a][cle]
                    motmax = cle
print(motmax)



