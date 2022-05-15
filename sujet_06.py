import random


def rendu(somme_a_rendre):
    n1 = somme_a_rendre // 5
    exce = somme_a_rendre % 5
    n2 = exce // 2
    n3 = exce % 2

    return [n1, n2, n3]


class Maillon:
    def __init__(self, v, suiv):
        """créé un maillon a la file"""
        self.valeur = v
        self.suivant = suiv


class File:
    def __init__(self):
        self.dernier_file = None

    def enfile(self, element):
        """ajoute un élément a la file"""
        nouveau_maillon = Maillon(element, self.dernier_file)
        self.dernier_file = nouveau_maillon

    def est_vide(self):
        """verifie si la file est vide"""
        return self.dernier_file is None

    def affiche(self):
        """affiche la file"""
        maillon = self.dernier_file
        while maillon is not None:
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self):
        """enleve un élément de la file"""
        if not self.est_vide():
            if self.dernier_file.suivant is None:
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file
            while maillon.suivant.suivant is not None:
                maillon = maillon.suivant
            resultat = maillon.suivant.valeur
            maillon.suivant = None
            return resultat
        return None


monnaie = random.randint(3, 50)
print(f'{monnaie} euro rend {rendu(monnaie)}')

F = File()
print(F.est_vide())

F.enfile(2)
F.affiche()

print(F.est_vide())

F.enfile(5)
F.enfile(7)
F.affiche()
print(F.defile())

print(F.defile())

F.affiche()
