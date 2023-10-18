from abc import ABC, abstractmethod

class BaseTriangle:
    @property
    def r_inscribed_circle(self):
        pass

    @property
    def r_circumscribed_circle(self):
        pass

    @property
    def area(self):
        pass

class EquilateralTriangle(BaseTriangle):
    def __init__(self):
        self._side = None
        self._r_inscribed_circle = None
        self._r_circumscribed_circle = None
        self._area = None

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, a):
        self._side = a
        self._r_inscribed_circle = (a * 3**0.5) / 6
        self._r_circumscribed_circle = a / 3**0.5
        self._area = (a**2 * 3**0.5)/4

    @property
    def r_inscribed_circle(self):
        return self._r_inscribed_circle

    @r_inscribed_circle.setter
    def r_inscribed_circle(self, r):
        self._side = (r * 6) / 3**0.5
        self._r_inscribed_circle = r
        self._r_circumscribed_circle = self._side / 3**0.5
        self._area = (self._side**2 * 3**0.5)/4

    @property
    def r_circumscribed_circle(self):
        return self._r_circumscribed_circle

    @r_circumscribed_circle.setter
    def r_circumscribed_circle(self, r):
        self._side = r * 3**0.5
        self._r_inscribed_circle = (self._side * 3**0.5) / 6
        self._r_circumscribed_circle = r
        self._area = (self._side**2 * 3**0.5)/4

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, s):
        self._side = (4 * S / 3**0.5)**0.5
        self._r_inscribed_circle = (self._side * 3 ** 0.5) / 6
        self._r_circumscribed_circle = self._side / 3 ** 0.5
        self._area = (self._side ** 2 * 3 ** 0.5) / 4

    def __str__(self):
        return f"side = {self.side}\n"\
               f"r_inscribed_circle = {self.r_inscribed_circle}\n"\
               f"r_circumscribed_circle = {self.r_circumscribed_circle}\n"\
               f"area = {self.area}\n"


if __name__ == "__main__":
    tri = EquilateralTriangle()
    tri.side = 5
    print(tri.r_circumscribed_circle)