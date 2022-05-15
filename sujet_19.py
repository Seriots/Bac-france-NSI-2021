from math import ceil

def recherche(tab, x):
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = ceil((debut+fin)/2)
        if x == tab[m]:
            return m
        if x > tab[m]:
            debut = m + 1
        else:
             fin = m - 1
    return -1

print(recherche([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],23))
print(recherche([2, 3, 4, 5, 6], 5))




ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    resultat = ''
    for lettre in message :
        if lettre in ALPHABET :
            indice = ( position_alphabet(lettre) + decalage )%26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat += lettre
    return resultat

print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !',4))
print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !',-5))