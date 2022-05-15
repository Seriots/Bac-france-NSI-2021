
def recherche(caractere, mot):
    result = 0
    for element in mot:
        if element == caractere:
            result += 1
    return result


print(recherche('i',"mississippi"))


pieces = [100,50,20,10,5,2,1]


def rendu_glouton(arendre, i=0, solution=[]):
    if arendre == 0:
       return solution
    p = pieces[i]
    if p <= arendre:
        return rendu_glouton(arendre - p, i, solution + [p])
    else :
        return rendu_glouton(arendre, i+1, solution)


print(rendu_glouton(291))
