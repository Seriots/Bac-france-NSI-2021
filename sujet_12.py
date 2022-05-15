
def maxi(tab):
    max = tab[0]
    i = 0
    max_i = 1
    for element in tab[1:]:
        i += 1
        if element > max:
            max = element
            max_i = i
    return max, max_i


print(maxi([1,5,6,9,1,2,3,10,9,8]))


def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n and trouve == False:
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j += 1
        if j == g:
            trouve = True
        i += 1
    return trouve

print(recherche("AATC", "GTACAAATCTTGCC"))
print(recherche("AGTC", "GTACAAATCTTGCC") )
