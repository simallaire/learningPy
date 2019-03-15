import numpy as np

def produit_vectoriel(a,b):
    A = np.matrix(a)
    B = np.matrix(b)
    print("A = \n"+ str(A),end="\n")
    print("B = \n"+ str(B),end="\n")
    return A*B

def produit_scalaire(a,b):
    A = np.matrix(a)
    B = np.matrix(b)
    print("A = \n"+ str(A),end="\n")
    print("B = \n"+ str(B),end="\n")
    return np.dot(A,B)


