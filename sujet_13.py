
from random import randint


def tri_selection(tab):
    for i in range(len(tab)):
        mini = tab[i]
        rang = i
        for j in range(i, len(tab)):
            if tab[j] < mini:
                mini = tab[j]
                rang = j
        x = tab[i]
        tab[rang] = x
        tab[i] = mini
        i += 1

    return tab

print(tri_selection([7,8,2, 1547,5,4,3]))



def plus_ou_moins():
    nb_mystere = randint(1,99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0

    while nb_mystere != nb_test and compteur < 10 :
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ",nb_mystere)
        print("Nombre d'essais: ",compteur)
    else:
        print ("Perdu ! Le nombre était ",nb_mystere)

plus_ou_moins()