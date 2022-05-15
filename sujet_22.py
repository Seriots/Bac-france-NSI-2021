import random


def recherche(a, t):
    result = 0
    for element in t:
        if element == a:
           result += 1
    return result


def rendu_monnaie_centimes(s_due, s_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = []
    a_rendre = s_versee-s_due
    i = len(pieces) - 1
    while a_rendre > 0 :
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre-pieces[i]
        else :
            i = i-1
    return rendu


print(recherche(5,[]))
print(recherche(5,[-2,3,4,8]))
print(recherche(5,[-2,3,1,5,3,7,4]))
print(recherche(5,[-2,5,3,5,4,5]))
l = [random.randint(1,10) for i in range(random.randint(0,10))]
print(l,recherche(1, l))

print(rendu_monnaie_centimes(700, 700))
print(rendu_monnaie_centimes(112, 500))
a = random.randint(10, 1000)
b = random.randint(500, 1500)
if b < a:
    b = a
print(a, b, rendu_monnaie_centimes(a, b))
