from AbstractMaker import AbstractMaker
from Harmonic import Harmonic

from Coords import Coords as Coordinates


class HarmonicMaker(AbstractMaker):

    # def __init__(self):
    #     pass

    def make(self, coords: Coordinates, *args):

        if len(args) < 4:
            raise Exception("Not enough parameters")
        elif args[0:4]:
            d0 = args[0]
            k = args[1]
            i = args[2]
            j = args[3]

            h_obj = Harmonic(coords, d0, k, i, j)

            return h_obj


if __name__ == "__main__":
    c1 = Coordinates("texts\drugi_przyklad")

    factory = HarmonicMaker()
    obj_h = factory.make(c1, 0, 1, 4, 5)
    print(obj_h)

    print(
        obj_h.energy()
    )

