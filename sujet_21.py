
def nb_repetitions(elt, tab):
    result = 0
    for element in tab:
        if element == elt:
            result += 1

    return result

print(nb_repetitions(12,[1, '! ',7,21,36,44]))



def binaire(a):
    bin_a = str(a % 2)
    a = a // 2
    while a > 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a

print(binaire(77))
