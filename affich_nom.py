# il faudra mettre les noms des présidents dans une liste listedoc
noms_prsdt=['Chirac', 'Chirac', 'Giscard dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Mitterrand', 'Sarkozy']
def nompresident(noms_prsdt):
    Listepres=[]
    #cpt pour n'afficher que la première occurence
    cpthollande = 0
    cptchirac = 0
    cptgiscard = 0
    cptmacron = 0
    cptsarkozy = 0
    cptmitterrand = 0
    for nom in noms_prsdt:
        if nom == 'Chirac' and cptchirac == 0 :
            Listepres.append(nom)
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

