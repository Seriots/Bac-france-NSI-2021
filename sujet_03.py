import random
from math import ceil

def oppose(n):
    value = n
    n -= value
    n -= value
    return n


def multiplication(n1, n2):
    result = 0
    switch = False
    if n2 < 0:
        switch = True
        n2 = oppose(n2)
    for i in range(n2):
        result += n1
    if switch:
        result = oppose(result)
    return result


print(multiplication(0, -8))


def dichotomie(tab, x):
    """
        tab : tableau d’entiers trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """

    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = ceil((debut+fin)/2)
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
             fin = m - 1
    return False

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],15))
