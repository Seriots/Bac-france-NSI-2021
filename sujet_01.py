import random
from math import sqrt

def recherche(tab, n):
    result = len(tab)
    if len(tab) > 0:
        for i in range (len(tab)):
            if tab[i] == n:
                result = i

        return result
    else:
        return 'liste vide'


l = [random.randint(0, 10) for i in range(random.randint(0, 10))]
print(l)
print(recherche(l, 1))

def distance(point1, point2):
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant à la plus
    courte distance du point depart."""
    point = tab[0]
    min_dist = distance(tab[0], depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart)< min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return [point[0], point[1]]


assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == [2, 5], "erreur"
print(plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)))