
def recherche(elt, tab):
    i = 0
    for element in tab:
        if elt == element:
            return i
        i += 1
    return -1

print(recherche(1, [1, 12, 1, 56]))



def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l)-2
    while a < l[i]:
        l[i+1] = l[i]
        l[i] = a
        i -= 1
    return l

print(insere(10,[1,2,7,12,14,25]))