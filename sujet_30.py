

def multiplication(n1, n2):
    result = 0
    switch = False
    if n2 < 0:
        switch = True
        n2 = 0-n2
    for i in range(n2):
        result += n1
    if switch:
        result = 0 - result
    return result


print(multiplication(-3, -8))
print(multiplication(4, -8))
print(multiplication(-3, 0))
print(multiplication(3, 5))
print(multiplication(0, 8))


def chercher(T,n,i,j):
    if i < 0 or j >= len(T):
        print("Erreur")
        return None
    if i > j:
        return None
    m = (i+j) // 2
    print(m, i, j)
    if T[m] < n:
        return chercher(T, n, m+1, j)
    elif T[m] > n:
        return chercher(T, n, i, m-1)
    else:
        return m


print(chercher([1,5,6,6,9,12],7,0,10))
print(chercher([1,5,6,6,9,12],7,0,5))
print(chercher([1,5,6,6,9,12],9,4,5))
print(chercher([1,5,6,6,9,12],6,0,5))