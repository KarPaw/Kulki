from abc import ABC, abstractmethod
from Coords import Coords as Coordinates


class AbstractMaker(ABC):

    @abstractmethod
    def make(self, coords: Coordinates, *args): pass
