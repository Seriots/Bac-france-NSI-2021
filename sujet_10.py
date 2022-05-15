
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


def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2

print(positif([-1,0,5,-3,4,-6,10,9,-8 ]))