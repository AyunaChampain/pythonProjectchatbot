from os import listdir

def list_of_files(directory, extension):
    files_names = []
    for filename in listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
def minuscules(repert) :
    list = list_of_files(repert, "txt")
    for i in range (len(list)) :
        with open("./speeches/" + list[i], 'r') as f :
            contenu = f.readlines()
            for line in contenu :
                new_line = ""
                for cara in line :
                    if ord(cara) >= 65 and ord(cara) <= 90 :
                        new_line += chr(ord(cara) + 32)
                    else :
                        new_line += cara
                with open("cleaned/" + list[i], "a") as f2 :
                    f2.write(new_line)

