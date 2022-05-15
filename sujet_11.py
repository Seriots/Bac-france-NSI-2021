
def conv_bin(value):
    i = 0
    result = []
    while value >= 2**i:
        i += 1
    i -= 1
    value -= 2**i
    result.append(1)
    for j in range(i):
        i -= 1
        print(value, 2**i)
        if value >= 2**i:
            value -= 2**i
            result.append(1)
        else:
            result.append(0)
    return result, len(result)


print(conv_bin(76))


def tri_bulles(T):
    n = len(T)
    for i in range(n,0,-1):
        for j in range(i-1):
            if T[j] > T[j+1]:
                x = T[j]
                T[j] = T[j+1]
                T[j+1] = x
    return T


def tri_bulles_2(T):
    n = len(T)+1
    for i in range(n-1):
        for j in range(i, 0, -1):
            if T[j] < T[j-1]:
                x = T[j-1]
                T[j-1] = T[j]
                T[j] = x
    return T

print(tri_bulles([8,7,6,154,4,3,2,1]))
print(tri_bulles_2([45,7,13,6,154,87,4,3,2,1]))