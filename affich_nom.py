def nompresident(noms_prsdt):
    #cpt pour n'afficher que la première occurence
    cpthollande = 0
    cptchirac = 0
    cptgiscard = 0
    cptmacron = 0
    cptsarkozy = 0
    cptmitterrand = 0
    for nom in noms_prsdt:
        if nom == 'Chirac' and cptchirac == 0 :
            return(nom)
            cptchirac = 1
        elif nom == 'Mitterrand' and cptmitterrand == 0 :
            return(nom)
            cptmitterrand = 1
        elif nom == 'Hollande' and cpthollande == 0 :
            return(nom)
            cpthollande = 1
        elif nom == 'Macron' and cptmacron == 0 :
            return(nom)
            cptmacron = 1
        elif nom == 'Sarkozy' and cptsarkozy == 0 :
            return(nom)
            cptsarkozy = 1
        elif nom == 'Giscard dEstaing' and cptgiscard == 0 :
            return(nom)
            cptgidcard = 1
