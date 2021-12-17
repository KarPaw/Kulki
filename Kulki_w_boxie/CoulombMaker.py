from AbstractMaker import AbstractMaker
from Coulomb import Coulomb

from Coords import Coords as Coordinates


#
class CoulombMaker(AbstractMaker):

    def make(self, coords: Coordinates, *args):

        if not args:
            raise Exception("Constant not provided")
        else:
            c = args[0]

            coul_obj = Coulomb(coords, c)

            return coul_obj


if __name__ == "__main__":
    c1 = Coordinates("texts\drugi_przyklad")

    factory = CoulombMaker()
    coul_obj = factory.make(c1, 1)
    print(coul_obj)

    print(
        coul_obj.energy()
    )
