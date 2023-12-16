# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot
# Retourne une liste des mots de la question en enlevant les ponctuations et majuscules
def mots_question(question):
    listedesmots=[]
    mot = question.split()
    mots=''
    for cara in question:
        if ord('A') <= ord(cara) <= ord('Z'):
            mots += chr(ord(cara) + 32)
        elif 31 >= ord(cara) >= 0 or 33 <= ord(cara) <= 45 or 47 <= ord(cara) <= 64 or 91>= ord(cara) >= 96 or 127 >= ord(cara)>= 123:
            mots += ' '
        elif ord(cara) == 32 or ord(cara) == 46:
            mots += ' '
        else:
            mots += chr(ord(cara))
        mot = mots.split()
    for mo in mot:
        if mo not in listedesmots and mo != " " and mo != "":
            listedesmots.append(mo)
    return listedesmots
