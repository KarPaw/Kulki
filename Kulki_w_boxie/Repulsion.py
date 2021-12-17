from Coords import Coords
from Energy import Energy
from itertools import combinations

class Repulsion(Energy):

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
                pair_energy = (float(atom1.r) + float(atom2.r) - atom1.distance_to(atom2))
                pe_2 = pair_energy * pair_energy
                pe_4 = pe_2 * pe_2
                # pair_energy_p6 - below
                total_energy += pe_4 * pe_2

        total_energy *= c

        return total_energy


if __name__ == "__main__":
    c1 = Coords("texts/drugi_przyklad")

    Col1 = Repulsion(c1, 1)

    print(
        Col1.energy()
    )
