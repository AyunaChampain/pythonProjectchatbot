def mots_question(question):
    listedesmots=[]
    mots = question.split()
    for i in range (len(question)):
        for cara in question:
            if (ord(cara) >= 33 and ord(cara) <= 38) or (ord(cara) >= 40 and ord(cara) <= 44) or (ord(cara) >= 46 and ord(cara) <= 47) or (ord(cara) >= 58 and ord(cara) <= 63) or (ord(cara) >= 91 and ord(cara) <= 96) or (ord(cara) >= 123 and ord(cara) <= 126):
                cara= " "
            elif (ord(cara) == 39) or (ord(cara) == 45):
                cara = " "
            print(question)
    if mots not in listedesmots and mots != " " and mots != "":
        listedesmots.append(mots)
    return listedesmots
laquest="je suis dans/ le salon."
a = mots_question(laquest)
print(a)
