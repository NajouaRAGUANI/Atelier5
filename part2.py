class Etudiant:

    nom = ""
    prenom = ""
    age = 0
    cne = ""
    moyenne = 0

    def _init_(self, nom="", prenom="", age=0, cne="", moyenne=0):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne
    def display(self):
        print(self.nom, "\t", self.prenom, "\t", self.age, "\t", self.cne, "\t", self.moyenne)


e1 = Etudiant("test", "test", 20, "9999", 15)
e2 = Etudiant("test", "test", 25, "9999", 12)
e3 = Etudiant("test", "test", 15, "9999", 17)
e4 = Etudiant("test", "test", 18, "9999", 20)
e5 = Etudiant("test", "test", 22, "9999", 10)
e6 = Etudiant("test", "test", 30, "9999", 16)

ListEtudiants = []
ListEtudiants.append(e1)
ListEtudiants.append(e2)
ListEtudiants.append(e3)
ListEtudiants.append(e4)
ListEtudiants.append(e5)
ListEtudiants.append(e6)

#sort selon l'age et la moyen :

def MySort1(etudiant):
    return -etudiant.moyenne - etudiant.age

#sort selon la moyen :

def MySort2(etudiant):
    return -etudiant.moyenne

#sort selon l'age  :

def MySort3(etudiant):
    return -etudiant.age

#affichage:
#sort selon l'age et la moyen :
ListEtudiants.sort(key=MySort1)
for i in ListEtudiants:
    i.display()
print("\n----------------------------------------\n")
#sort selon la moyen :
ListEtudiants.sort(key=MySort2)
for i in ListEtudiants:
    i.display()
print("\n----------------------------------------\n")
#sort selon la l'age :
ListEtudiants.sort(key=MySort3)
for i in ListEtudiants:
    i.display()
