from Coords import Coords
from Energy import Energy
from itertools import combinations

class Coulomb(Energy):

    def __init__(self, coords_object, c):

        self.__c = c
        if isinstance(coords_object, Coords):
            self.__coords_object = coords_object
        else:
            raise Exception("parameter is not a Coords_Object")

    @property
    def get_c(self):
        return self.__c

    def energy(self):

        c = self.get_c
        coords_object = self.__coords_object

        pary_atomow = combinations(coords_object, 2)


        total_energy = 0
        for atom1, atom2 in pary_atomow:
            if not atom1.distance_to(atom2) == 0:
                pair_energy = (float(atom1.q) * float(atom2.q)) / atom1.distance_to(atom2)
                total_energy += pair_energy

        total_energy *= c

        return total_energy


if __name__ == "__main__":
    c1 = Coords("texts/drugi_przyklad")

    Col1 = Coulomb(c1, 1)

    print(
        Col1.energy()
    )
