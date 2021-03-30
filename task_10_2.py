from abc import ABC, abstractmethod


class Clothing(ABC):
    res = 0

    def __init__(self, par):
        self.par = par

    @property
    @abstractmethod
    def consuming(self):
        pass

    def __add__(self, other):
        Clothing.res += self.consuming + other.consuming
        return Costume(0)

    def __str__(self):
        result = Clothing.res
        Clothing.res = 0
        return f'{result}'


class Coat(Clothing):
    @property
    def consuming(self):
        return round(self.par / 6.5) + 0.5


class Costume(Clothing):
    @property
    def consuming(self):
        return round((2 * self.par + 0.3) / 100)


coat = Coat(43)
costume = Costume(181)
print(coat + costume + coat)