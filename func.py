import numpy as np

def oneMatr(N):
    oneMatr = np.ones((N, N), dtype=np.int32)
    return oneMatr


def randMatr(N):
    matr = np.random.randint(0, 10, (N, N))
    return matr


def oneVector(N):
    oneVector = np.ones(N, dtype=np.int32)
    return oneVector


def randVect(N):
    Vect = np.random.randint(0, 10, N)
    return Vect


def multMatr(matr1, matr2):
    multMatr = matr1.dot(matr2)
    return multMatr


def scalarMult(vect1, vect2):
    multVector = sum(p * q for p, q in zip(vect1, vect2))
    return multVector


def minVect(vect):
    minVect = min(vect)
    return minVect


def scalarMultMatr(a, matr):
    scalarMultMatr = a * matr
    return scalarMultMatr


def Mult(a, b):
    c = a * b
    return c


def sumMatr(matr1, matr2):
    sumMatr = matr1 + matr2
    return sumMatr
