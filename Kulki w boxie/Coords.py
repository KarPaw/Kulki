from Atom import Atom


class Coords:

    def __init__(self, file):
        # To powinien byc loop wywolujacy kilka razy konstruktor
        # klasy ATOM

        slownik_wszystkich_atomow = self.slownik_atomow(file)
        # print(slownik_wszystkich_atomow)

        # atomy = list(len(slownik_wszystkich_atomow['id']) * [None])
        atomy = list(len(slownik_wszystkich_atomow['id']) * [None])
        print(atomy)
        for i in range(len(slownik_wszystkich_atomow['id'])):
            potrzebne_do_stworzenia_atomu = (slownik_wszystkich_atomow["id"][i],
                                             slownik_wszystkich_atomow["x"][i],
                                             slownik_wszystkich_atomow["y"][i],
                                             slownik_wszystkich_atomow["r"][i],
                                             slownik_wszystkich_atomow["m"][i])

            # Tu tworzymy atomy z konstruktora
            atomy[i] = Atom(*potrzebne_do_stworzenia_atomu)
        # print(atomy)

        print(atomy)
        self.__atomy = atomy

    @staticmethod
    def slownik_atomow(plik):

        slownik = {"id": [],
                   "x": [],
                   "y": [],
                   "r": [],
                   "m": []}

        with open(plik) as f:
            line = iter(f)
            next(line)  # pomijamy pierwsza linijke pliku, czyli naglowek
            for line in f:
                if line[0] == "#":
                    [slownik[klucz].append(None) for klucz in slownik.keys()]

                else:
                    lista_wyrazow_w_linii = line.split()

                    if len(lista_wyrazow_w_linii) != 5:
                        # zamiast wadliwych wynijek dajemy None
                        [slownik[klucz].append(None) for klucz in slownik.keys()]

                    # slownik["id"].append(lista_wyrazow_w_linii[0])
                    # slownik["x"].append(lista_wyrazow_w_linii[1])
                    # slownik["y"].append(lista_wyrazow_w_linii[2])
                    # slownik["r"].append(lista_wyrazow_w_linii[3])
                    # slownik["m"].append(lista_wyrazow_w_linii[4])

                    [slownik[list(slownik.keys())[krotka[0]]].append(krotka[1]) for krotka in enumerate(lista_wyrazow_w_linii)]

        return slownik

    def __str__(self):

        # Atom str
        return f"Atom\\ID:{self.__id}, X:{self.__x}, Y:{self.__y}"

    def get_position(self):
        ...

    # do zrobienia
    def ITERATOR(self):
        if ...:
            ...


if __name__ == "__main__":
    Coords("drugi_przyklad")
    # print(type(Coords("drugi_przyklad").__atomy))
    # lista_atomow = Coords("drugi_przyklad").__atomy
    # print(lista_atomow)
    # print(type(lista_atomow))
    # a1 = Coords("drugi_przyklad").atomy[0]
    # print(a1)
    # # print(a1.get_position())
    # print("HOOH")
    # print(Coords("drugi_przyklad"))

