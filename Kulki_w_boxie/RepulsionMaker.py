from AbstractMaker import AbstractMaker
from Repulsion import Repulsion

from Coords import Coords as Coordinates


#
class RepulsionMaker(AbstractMaker):

    def make(self, coords: Coordinates, *args):

        if not args:
            raise Exception("Constant not provided")
        else:
            c = args[0]

            repul_obj = Repulsion(coords, c)

            return repul_obj


if __name__ == "__main__":
    c1 = Coordinates("texts\drugi_przyklad")

    factory = RepulsionMaker()
    rep_obj = factory.make(c1, 1)
    print(rep_obj)

    print(
        rep_obj.energy()
    )
