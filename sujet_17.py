def rechercheMin(tab):
    mini = tab[0]
    for element in tab[1:]:
        if element < mini:
            mini = element

    return tab.index(mini)


print(rechercheMin([2, 4, 1]))


def separe(tab):
    i = 0
    j = len(tab)-1
    while i != j:
        if tab[i] == 0:
            i += 1
        else:
            tab[j], tab[i] = 1, tab[j]
            j -= 1
    return tab

print(separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]))