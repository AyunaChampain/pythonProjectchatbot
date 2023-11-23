import os

def minuscules(file) :

    with open(file, 'r') as f :
        contenu = f.readlines()
        for line in contenu :
            new_line = ""
            for cara in line :
                if ord(cara) >= 65 and ord(cara) <= 90 :
                    new_line += chr(ord(cara) + 32)
                else :
                    new_line += cara
            with open("cleaned/file.txt", "a") as f2 :
                f2.write(new_line)

