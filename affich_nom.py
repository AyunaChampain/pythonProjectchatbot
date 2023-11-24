# il faudra mettre les noms des présidents dans une liste listedoc
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
            return(nom, end= " ")
            cptchirac = 1
        elif nom == 'Mitterrand' and cptmitterrand == 0 :
            return(nom, end=" ")
            cptmitterrand = 1
        elif nom == 'Hollande' and cpthollande == 0 :
            return(nom, end=" ")
            cpthollande = 1
        elif nom == 'Macron' and cptmacron == 0 :
            return(nom, end=" ")
            cptmacron = 1
        elif nom == 'Sarkozy' and cptsarkozy == 0 :
            return(nom, end=" ")
            cptsarkozy = 1
        elif nom == 'Giscard dEstaing' and cptgiscard == 0 :
            return(nom, end=" ")
            cptgidcard = 1
