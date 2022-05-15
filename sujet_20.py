
t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]


def mini(t_moy, annees):
    minimum = t_moy[0]
    i =0
    result = minimum, annees[i]
    for element in t_moy[1:]:
        i += 1
        if element<minimum:
            minimum = element
            result = element, annees[i]

    return result

print(mini(t_moy, annees))


def inverse_chaine(chaine):
    result = ''
    for caractere in chaine:
        result = caractere + result
    return result


def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse == chaine


def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)


print(inverse_chaine('bac'))
print(est_palindrome('NSI'))
print(est_palindrome('ISN-NSI'))
print(est_nbre_palindrome(214312))
print(est_nbre_palindrome(213312))