class Point:  #définition classe point
    x = 0
    y = 0

    def _init_(self, x=0, y=0):
        self.x = x
        self.y = y


class Segment:  #classe en utilisant classe point
    orig = Point(0, 0)
    extrem = Point(0, 0)

    def _init_(self, Xo=0, Yo=0, Xe=0, Ye=0 ):
        self.orig.x = Xo
        self.orig.y = Yo
        self.extrem.x = Xe
        self.extrem.y = Ye

    def display(self):
        print("l’origine : (", self.orig.x, ", ", self.orig.y, ")  l’extrémité : (", self.extrem.x, ", ", self.extrem.y, ")")


o = Point(1, 1)
e = Point(2, 2)
s = Segment(0, 1, 2, 3)
s.display()
