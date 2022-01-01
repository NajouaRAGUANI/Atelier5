class Rectangle: #définition classe réctangle

    l = 0
    h = 0
    nom = ""

    def _init_(self, l=0, h=0, nom='rectangle'):  #initialisation avec valeurs par défaut
        self.l = l
        self.h = h
        self.nom = nom

    def display(self):
        print("(", self.nom, ": (", self.l, ", ", self.h, ")")

    def surface(self):
        return self.l*self.h


class Carre(Rectangle):  #classe des carres

     def _init_(self, l=0, h=0, nom='Carre'):
        super()._init_(l, h)
        self.nom = nom


c = Carre(2, 2, 'carre1')
r = Rectangle(9, 9, 'rectangle1')
