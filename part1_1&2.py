class Vecteur2D:   #définition class vecteur2D

    x = 0
    y = 0

    def _init_(self, x=0, y=0):  #constructeur avec parametre par défaut
        self.x = x  #initialisation de x et y
        self.y = y

    def display(self):
        print("(", self.x, ", ", self.y, ")")

    def _add_(self, other):
        a = self.x + other.x
        b = self.y + other.y
        v = Vecteur2D(a,b)
        return v


vec = Vecteur2D()
vec2 = Vecteur2D(4 , 5)
vec.x = 1
vec.y = 9
vec.display()
vec2.display()
vec3 = vec + vec2
vec3.display()
