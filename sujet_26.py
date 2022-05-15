

def occurence_max(phrase):
    result = {}
    for element in phrase:
        if element in alphabet:
            if element not in result:
                result[element] = 0
            result[element] += 1
    maxi = 0
    for element in result.items():
        if element[1] > maxi:
            maxi = element[1]
            result = element[0]
    return result


ch= 'je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(occurence_max(ch))


def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)


def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])


def negatif(image):
    '''renvoie le négatif de l'image sous la forme
       d'une liste de listes'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on créé une image de 0 aux mêmes dimensions que le paramètre image
    for i in range(len(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255 - image[i][j]
    return L


def binaire(image, seuil):
    '''renvoie une image binarisée de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inférieure au seuil
       et 1 sinon'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on crée une image de 0 aux mêmes dimensions que le paramètre image
    for i in range(len(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil:
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L


img= [[20, 34, 254, 145, 6], [23, 124, 287, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
img_neg = negatif(img)
print(img_neg)
print(binaire(img_neg, 120))
