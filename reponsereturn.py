def repreturn(docpertinent,motquestioneleve):
    docpertinent = docpertinent.replace("-",".")
    docpertinent = docpertinent.replace("!",".")
    docpertinent = docpertinent.replace("?",".")
    a = docpertinent.split(".")
    cpt = 0
    for sentence in a:
        if motQuestionEleve in a and cpt == 0:
            cpt = 1
            return a




