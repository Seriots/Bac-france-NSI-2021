import random


def recherche(l):
    result = []
    for i in range(len(l)-1):
        if l[i] == l[i + 1] + 1 or l[i] == l[i + 1] - 1:
            tuple_ = (l[i], l[i + 1])
            result.append(tuple_)
    return result


def propager(M, i, j, val):
    if M[i][j] == 0:
        return
    M[i][j] = val
    if (i - 1)>=0 and M[i - 1][j] == 1:
        propager(M, i-1, j, val)

    if (i + 1)<len(M) and M[i + 1][j] == 1:
        propager(M, i+1, j, val)

    if (j - 1)>=0 and M[i][j-1] == 1:
        propager(M, i, j-1, val)

    if (j + 1)<len(M) and M[i][j+1] == 1:
        propager(M, i, j+1, val)

m = [[random.choice((0,1)) for k in range(4)],[random.choice((0,1)) for k in range(4)],[random.choice((0,1)) for k in range(4)],[random.choice((0,1)) for k in range(4)]]
k = random.randint(0, 3)
j = random.randint(0,3)
propager(m, j,k, 3)
print(k, j, m)


l = [random.randint(-10, 10) for i in range(10)]
print(l)
print(recherche(l))
