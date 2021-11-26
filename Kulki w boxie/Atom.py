class Atom:

    # x, y, m, r
    def __init__(self, id, x, y, m=1, r=1):

        # id atomu

        self.__id = id

        # polozenie atomu
        self.__x = x
        self.__y = y

        # masa
        self.m = m
        # promien
        self.r = r

    def set(self, x, y):
        # umozliwia zmiane wspolrzednych X oraz Y

        self.__x = x
        self.__y = y

    @property
    def get_position(self):
        return self.__x, self.__y

    def __str__(self):

        return f"Atom\\ID:{self.__id}, X:{self.__x}, Y:{self.__y}"



if __name__ == "__main__":
    a1 = Atom(2, 4, 1, 1)
    a2 = Atom(5, 7, 2, 1)

    print(a1.get_position)
    a1.set(0,0)
    print(a1.get_position)


    # print(a2.get_position)
    # print(type(a2.get_position))


