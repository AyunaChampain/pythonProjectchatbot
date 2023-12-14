# Champain Ayuna, Tea Julia, Teyssedre Orphée --- Groupe C
# Projet Python : My First ChatBot

def mots_question(question):
    listedesmots=[]
    mots = question.split()
    mot=''
    for cara in question:
        if ord('A') <= ord(cara) <= ord('Z'):
            mot += chr(ord(cara) + 32)
        elif 31 >= ord(cara) >= 0 or 33 <= ord(cara) <= 45 or 47 <= ord(cara) <= 64 or 91>= ord(cara) >= 96 or 127 >= ord(cara)>= 123:
            mot += ''
        elif ord(cara) == 32 or ord(cara) == 46:
            mot += ' '
        else:
            mot += chr(ord(cara))
        mots = mot.split()
    for mo in mots:
        if mo not in listedesmots and mo != " " and mo != "":
            listedesmots.append(mo)
    return listedesmots
