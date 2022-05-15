import random


def recherche(elt, l):
    i = 0
    result = -1
    for element in l:
        if element == elt:
            result = i
        i+=1

    return result


class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse

    def list_octet(self):
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        return True if self.adresse == '192.168.0.0' or self.adresse == '192.168.0.255' else False

    def adresse_suivante(self):
        list_octet = self.list_octet()
        if list_octet[3]< 254:
            octet_nouveau = 1+list_octet[3]
            return AdresseIP(f'192.168.0.{octet_nouveau}')
        else:
            return False



l = [random.randint(1, 10) for i in range(10)]
elt = random.randint(1,10)
adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2')
adresse3 = AdresseIP('192.168.0.0')
print(elt, l,recherche(elt, l))

print(adresse1.est_reservee())
print(adresse3.est_reservee())
print(adresse2.adresse_suivante().adresse)