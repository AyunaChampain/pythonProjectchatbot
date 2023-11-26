from Functions import *

def listemots(tf):
    a=[]
    for i in tf:
        for cle in i.keys():
            a.append(cle)
    print(a)

var = tf("./cleaned")
listemots(var)

"""from extrairenoms import *
def oups(b):
    print(b)
b= nom("./cleaned")
oups(b)"""