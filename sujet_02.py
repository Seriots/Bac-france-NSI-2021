import random


def moyenne(tab):
    result = 0
    if len(tab)>0:
        for element in tab:
            result += element
        result /= len(tab)
        return result
    else:
        return 'erreur'


l = [random.randint(0, 20) for i in range(15)]
print(l)
print(moyenne(l))


def tri(tab):
    #i est le premier indice de la zone non triee, j le dernier indice.
    #Au debut, la zone non triee est le tableau entier.
    i = 0
    j = len(tab)-1
    while i != j:
        if tab[i] == 0:
            i += 1
        else:
            valeur = tab[j]
            tab[j] = 1
            tab[i] = valeur
            j -= 1
    return tab


l = [random.randint(0, 1) for y in range(15)]
print(l)
print(tri(l))