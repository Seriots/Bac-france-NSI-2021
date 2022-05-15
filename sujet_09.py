

def moyenne(notes):
    result = 0
    coeff_tot = 0
    for element in notes:
        result += element[0]*element[1]
        coeff_tot += element[1]
    print(result, coeff_tot)
    result /= coeff_tot
    return result

print(moyenne([(15,2),(9,1),(12,3)]))


def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C

print(pascal(24))
