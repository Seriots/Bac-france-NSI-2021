
def moyenne(tab):
    result= 0
    for element in tab:
        result += element
    result /= len(tab)
    return result

print(moyenne([1.0, 2.0, 4.0]))


def dec_to_bin(a):
    bin_a = str(a % 2)
    a = a//2
    while a > 0 :
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a

print(dec_to_bin(128))