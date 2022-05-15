import random
from math import ceil

def moyenne(tab):
    result = 0
    if len(tab)>0:
        for element in tab:
            result += element
        result /= len(tab)
        return result
    else:
        return 'erreur'

assert moyenne([1]) == 1
assert moyenne([1,2,3,4,5,6,7]) == 4
assert moyenne([1,2]) == 1.5
l = [random.randint(0, 20) for i in range(15)]
print(l)
print(moyenne(l))




def dichotomie(tab, x):
    """
        tab : tableau trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if len(tab) == 0:
        return False, 1

    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or x > tab[-1]:
        return False, 2

    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = ceil((debut + fin) / 2)
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False, 3

print(dichotomie([],28))
