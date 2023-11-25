from extrairenoms import *

def ponctuation(reper):
    dico = {}
    M = []
    list = list_of_files(reper, "txt")
    for i in range(len(list)):
        new_line2 = ""
        with open("./cleaned/" + list[i], 'r') as f3:
            contenu2 = f3.readlines()
            for lines in contenu2 :
                for cara2 in lines :
                    if (ord(cara2) >= 33 and ord(cara2) <= 38) or (ord(cara2) >= 40 and ord(cara2) <= 44) or (ord(cara2) >= 46 and ord(cara2) <= 47) or (ord(cara2) >= 58 and ord(cara2) <= 63) or (ord(cara2) >= 91 and ord(cara2) <= 96) or (ord(cara2) >= 123 and ord(cara2) <= 126):
                        new_line2 += " "
                    elif (ord(cara2) == 39) or (ord(cara2) == 45):
                        new_line2 += " "
                    else:
                        new_line2 += cara2
            with open("./cleaned/" + list[i], "w") as f4 :
                f4.write(new_line2)

