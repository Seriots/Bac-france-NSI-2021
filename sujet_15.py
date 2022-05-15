import random


def rechercheMinMax(tab):
    result = {'min':tab[0], 'max':tab[0]}
    for element in tab:
        if element < result['min']:
            result['min'] = element
        elif element > result['max']:
            result['max'] = element

    return result

tableau = [-25, 1, 4, 2, -2, 9, 3, 1, 7, 25]
print(rechercheMinMax(tableau))



class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10, 
       Valet, Dame, Roi"""
    def getNom(self):
        if 1 < self.Valeur < 11:
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle'][self.Couleur]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []
        self.liste_carte = []
        for j in range(0, 4):
            self.liste_carte += [(j, i) for i in range(1, 14)]

    """Remplit le paquet de cartes"""
    def remplir(self):
        for i in range(52):
            x = random.choice(self.liste_carte)
            self.liste_carte.remove(x)
            nom, couleur = x
            carte = Carte(nom, couleur)
            self.contenu.append(carte)

        for element in self.contenu:
            print(element.getNom() + " de " + element.getCouleur()+'\n')

    """Renvoie la Carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        return self.contenu[pos-1]



unPaquet = PaquetDeCarte()
unPaquet.remplir()
uneCarte = unPaquet.getCarteAt(1)
print(uneCarte.getNom() + " de " + uneCarte.getCouleur()+'\n')