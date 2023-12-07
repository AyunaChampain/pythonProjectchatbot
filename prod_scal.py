#mettre A pour la question et B la matrice
def prod_scal():
    sommeAB = 1
    for i in range(len(A)):  #//len(M)
        sommeAB = A[i]*B[i]  #pck B c'est une ligne nan?
    return sommeAB