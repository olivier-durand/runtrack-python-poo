#Créer une classe Rectangle avec des attributs privés, longueur et largeur initialisées dans le constructeur

class Rectangle:

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    #Créer des assesseurs et mutateurs afin de pouvoir afficher et modifier les attributs de la classe
    def get_longueur(self):
        return self.__longueur

    def set_longueur (self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur (self, largeur):
        self.__largeur = largeur

#Changer la valeur de la longueur et de la largeur et vérifier que les modifications soient bien prises

rectangle = Rectangle(10,5)
print(rectangle.get_longueur())
print(rectangle.get_largeur())

rectangle.set_longueur(12)
rectangle.set_largeur(5)

print(rectangle.get_longueur())
print(rectangle.get_largeur())
